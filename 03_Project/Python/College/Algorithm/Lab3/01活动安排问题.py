#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
活动安排问题（活动选择问题）—— 贪心算法

问题：给定 n 个活动的集合 S = {a1, a2, ..., an}，每个活动 ai 都有一个
      起始时间 start_i 和结束时间 finish_i（start_i < finish_i）。若两个
      活动 ai、aj 满足 start_i >= finish_j 或 start_j >= finish_i，则称二者
      相容（时间区间不重叠）。活动安排问题要求在 S 中选出最大的相容活动
      子集（即占用同一资源的活动数最多）。

贪心策略：按结束时间 finish_i 非减序排列，依次考察每个活动，
          只要它与"最近被选中的活动"相容，就把它选入解集。

运行方式：
    python "01活动安排问题.py"            交互式功能演示
    python "01活动安排问题.py" --check    自动功能对拍测试
    python "01活动安排问题.py" --bench    性能测试（输出 CSV 数据）

--bench 可附加参数：
    --n 1000,2000,5000     指定测试规模（逗号分隔）
    --repeat 5             每个规模重复次数（取中位数）
    --seed 2024            随机数种子
    --out bench_activity.csv   CSV 输出路径
"""

from __future__ import annotations

import argparse
import csv
import os
import random
import statistics
import sys
import time
from dataclasses import dataclass
from typing import List, Optional, Sequence, Tuple


# ----------------------------------------------------------------------------
# 一、数据结构定义
# ----------------------------------------------------------------------------
@dataclass(frozen=True)
class Activity:
    """一个活动：编号、起止时间与可读名称。"""

    idx: int
    start: int
    finish: int
    name: str = ""

    def __post_init__(self) -> None:
        if self.start >= self.finish:
            raise ValueError(f"活动 {self.name or self.idx} 的起始时间必须小于结束时间")

    @property
    def duration(self) -> int:
        return self.finish - self.start

    def compatible_with(self, other: "Activity") -> bool:
        """两个活动时间区间不重叠即相容。"""
        return self.start >= other.finish or other.start >= self.finish

    def __str__(self) -> str:
        tag = self.name or f"a{self.idx}"
        return f"{tag}[{self.start}, {self.finish})"


# ----------------------------------------------------------------------------
# 二、贪心算法主体
# ----------------------------------------------------------------------------
def greedy_activity_selector(
    activities: Sequence[Activity], trace: Optional[List[str]] = None
) -> List[Activity]:
    """
    迭代版贪心算法（按结束时间最早优先）。

    时间复杂度：排序 O(n log n) + 单趟扫描 O(n)  =>  O(n log n)
    空间复杂度：排序副本 O(n)（Python 的 sorted 为 Timsort，需要 O(n) 辅助空间）

    参数
    ----
    activities : 活动序列（任意顺序）
    trace      : 若给出列表，则把每一步的决策记录进去，便于演示

    返回
    ----
    被选中的活动列表（按结束时间升序）
    """
    # 第 1 步：按结束时间非减序排序；结束时间相同则按开始时间升序，保证结果确定
    ordered = sorted(activities, key=lambda a: (a.finish, a.start))
    if trace is not None:
        trace.append("按结束时间排序后：" + "、".join(str(a) for a in ordered))

    chosen: List[Activity] = []
    last_finish = None  # 最近一次被选中活动的结束时间

    # 第 2 步：线性扫描，贪心地"能选就选"
    for act in ordered:
        if last_finish is None or act.start >= last_finish:
            prev = last_finish
            chosen.append(act)
            last_finish = act.finish
            if trace is not None:
                trace.append(f"选中 {act}：开始时间 {act.start} >= "
                             f"{'−∞' if prev is None else prev}（上一选中活动结束时间）")
        else:
            if trace is not None:
                trace.append(f"跳过 {act}：与已选活动冲突"
                             f"（{act.start} < {last_finish}）")

    return chosen


def greedy_recursive(
    ordered: Sequence[Activity], k: int = 0, last_finish: int = -1,
    acc: Optional[List[Activity]] = None
) -> List[Activity]:
    """
    递归版贪心（与迭代版等价，用于验证"贪心选择 + 最优子结构"的递归表述）。

    递推式：设活动已按结束时间排序，f(k) 表示"在前 k 个活动已选定的前提下，
    从第 k 个之后继续安排"的解，则
        f(k) = 若 a_k 与已选集合相容，则 {a_k} ∪ f(next(k))，否则 f(k+1)
    该递归每层只做常数工作，递归深度不超过 n。
    """
    if acc is None:
        acc = []
    if k >= len(ordered):
        return acc
    act = ordered[k]
    if act.start >= last_finish:
        acc.append(act)
        return greedy_recursive(ordered, k + 1, act.finish, acc)
    return greedy_recursive(ordered, k + 1, last_finish, acc)


# ----------------------------------------------------------------------------
# 三、用于对拍的正确性基准（精确最优解）
# ----------------------------------------------------------------------------
def optimal_count_dp(activities: Sequence[Activity]) -> int:
    """
    动态规划求最大相容活动数（精确最优解），用于与贪心结果对拍。

    设活动按结束时间排序后为 a1..an，p(i) 为"结束时间不晚于 a_i 开始时间"
    的最大下标，则
        dp[i] = max(dp[i-1], 1 + dp[p(i)]),  dp[0] = 0
    时间复杂度 O(n log n)，空间 O(n)。本函数作为独立的"另一条思路"实现，
    与贪心的实现细节完全解耦，因此可以用来交叉验证贪心的最优性。
    """
    ordered = sorted(activities, key=lambda a: (a.finish, a.start))
    n = len(ordered)
    if n == 0:
        return 0
    finishes = [a.finish for a in ordered]
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        # p = 满足 finishes[p-1] <= ordered[i-1].start 的最大活动数
        p = _bisect_right(finishes, ordered[i - 1].start, hi=i - 1)
        dp[i] = max(dp[i - 1], 1 + dp[p])
    return dp[n]


def _bisect_right(arr: Sequence[int], x: int, hi: int) -> int:
    """在手写二分中返回 arr[0:hi] 中 <= x 的元素个数（避免依赖 bisect 的细节）。"""
    lo, right = 0, hi
    while lo < right:
        mid = (lo + right) // 2
        if arr[mid] <= x:
            lo = mid + 1
        else:
            right = mid
    return lo


def optimal_count_bruteforce(activities: Sequence[Activity]) -> int:
    """
    位掩码穷举求最大相容活动数（n <= 15 时使用），用于第二重对拍。

    枚举所有 2^n 个子集，对每个子集检查两两相容性，取最大基数。
    复杂度 O(2^n · n^2)，仅用于小规模验证。
    """
    n = len(activities)
    best = 0
    for mask in range(1 << n):
        cnt = bin(mask).count("1")
        if cnt <= best:
            continue  # 剪枝：不可能更优
        picked = [activities[i] for i in range(n) if mask >> i & 1]
        if all(picked[i].compatible_with(picked[j])
               for i in range(len(picked)) for j in range(i + 1, len(picked))):
            best = cnt
    return best


def alternative_greedy(activities: Sequence[Activity], key: str) -> List[Activity]:
    """
    另外两种"看起来合理"的贪心策略，用于说明贪心策略选择的必要性：
      key = "start"    : 每次选开始时间最早的活动
      key = "duration" : 每次选持续时间最短的活动
    二者均不保证最优。
    """
    if key == "start":
        ordered = sorted(activities, key=lambda a: (a.start, a.finish))
    elif key == "duration":
        ordered = sorted(activities, key=lambda a: (a.duration, a.finish))
    else:
        raise ValueError("key 只能是 'start' 或 'duration'")
    chosen: List[Activity] = []
    for act in ordered:
        if all(act.compatible_with(c) for c in chosen):
            chosen.append(act)
    return chosen


# ----------------------------------------------------------------------------
# 四、输入解析与结果格式化
# ----------------------------------------------------------------------------
def parse_activities(text: str) -> List[Activity]:
    """
    解析形如 "1 4, 3 5, 0 6" 的活动串（每项 "开始 结束"）。也支持每行一个活动。
    返回按输入顺序编号的活动列表。
    """
    items = []
    for chunk in text.replace("；", ",").replace("，", ",").replace("\n", ",").split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        parts = chunk.replace("-", " ").replace("~", " ").split()
        if len(parts) != 2:
            raise ValueError(f"无法解析活动 '{chunk}'，应形如 '1 4'")
        items.append((int(parts[0]), int(parts[1])))
    return [Activity(i + 1, s, f, f"a{i + 1}") for i, (s, f) in enumerate(items)]


def random_activities(
    n: int, horizon: int = 100, rng: Optional[random.Random] = None
) -> List[Activity]:
    """随机生成 n 个活动：起点在 [0, horizon)，长度在 [1, horizon//4]。"""
    rng = rng or random.Random()
    acts = []
    for i in range(n):
        s = rng.randrange(0, horizon)
        d = rng.randrange(1, max(2, horizon // 4))
        acts.append(Activity(i + 1, s, s + d, f"a{i + 1}"))
    return acts


def format_schedule(acts: Sequence[Activity]) -> str:
    return "、".join(str(a) for a in acts)


# ----------------------------------------------------------------------------
# 五、交互式演示
# ----------------------------------------------------------------------------
def demo_textbook() -> None:
    """教材经典算例：11 个活动，最大相容子集大小为 4。"""
    data = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9),
            (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    acts = [Activity(i + 1, s, f, f"a{i + 1}") for i, (s, f) in enumerate(data)]
    print("\n[算例] 教材经典算例（11 个活动，按输入编号 a1..a11）")
    print(f"{'活动':<6}{'开始':>6}{'结束':>6}{'持续时间':>10}")
    for a in acts:
        print(f"{a.name:<6}{a.start:>6}{a.finish:>6}{a.duration:>10}")
    trace: List[str] = []
    chosen = greedy_activity_selector(acts, trace)
    print("\n[贪心执行过程]")
    for line in trace:
        print("  " + line)
    print(f"\n[贪心结果] 共选中 {len(chosen)} 个活动：{format_schedule(chosen)}")
    print(f"[动态规划最优值] {optimal_count_dp(acts)}")
    print(f"[穷举最优值]     {optimal_count_bruteforce(acts)}")
    alt_s = alternative_greedy(acts, "start")
    alt_d = alternative_greedy(acts, "duration")
    print(f"[对比] 按开始时间贪心 {len(alt_s)} 个；按持续时间贪心 {len(alt_d)} 个")


def demo_manual() -> None:
    """手工输入活动。"""
    print("\n请输入活动，格式为 '开始 结束'，多个活动用逗号分隔，例如：1 4, 3 5, 0 6")
    raw = input("活动列表：").strip()
    if not raw:
        print("未输入内容，返回主菜单。")
        return
    acts = parse_activities(raw)
    trace: List[str] = []
    chosen = greedy_activity_selector(acts, trace)
    for line in trace:
        print("  " + line)
    print(f"\n最大相容活动数为 {len(chosen)}：{format_schedule(chosen)}")
    print(f"校验：DP 最优值 = {optimal_count_dp(acts)}，"
          f"贪心是否最优 = {len(chosen) == optimal_count_dp(acts)}")


def demo_random() -> None:
    """随机算例：对比三种贪心策略与最优解，并统计各策略的"次优率"。"""
    n = input("随机活动个数（默认 12）：").strip()
    n = int(n) if n else 12
    rng = random.Random()
    acts = random_activities(n, horizon=max(6, n), rng=rng)
    print("\n[随机算例] " + format_schedule(acts))
    opt = optimal_count_dp(acts)
    res = {
        "按结束时间最早（本文策略）": greedy_activity_selector(acts),
        "按开始时间最早": alternative_greedy(acts, "start"),
        "按持续时间最短": alternative_greedy(acts, "duration"),
    }
    print(f"{'策略':<26}{'选中数':>8}{'是否最优':>10}   选中序列")
    for name, chosen in res.items():
        print(f"{name:<26}{len(chosen):>8}{'是' if len(chosen) == opt else '否':>10}   "
              f"{format_schedule(chosen)}")
    print(f"\n最优值（动态规划）= {opt}；穷举值 = {optimal_count_bruteforce(acts)}")

    # 统计：在 800 个随机实例上，三种准则分别有多大比例得不到最优解
    stat_rng = random.Random(2024)
    trials = 800
    fail = {"按结束时间最早（本文策略）": 0, "按开始时间最早": 0, "按持续时间最短": 0}
    for _ in range(trials):
        a = random_activities(stat_rng.randint(4, 14), horizon=16, rng=stat_rng)
        best = optimal_count_dp(a)
        if len(greedy_activity_selector(a)) != best:
            fail["按结束时间最早（本文策略）"] += 1
        if len(alternative_greedy(a, "start")) != best:
            fail["按开始时间最早"] += 1
        if len(alternative_greedy(a, "duration")) != best:
            fail["按持续时间最短"] += 1
    print(f"\n[统计] {trials} 个随机实例上各准则未达最优的比例：")
    for name, cnt in fail.items():
        print(f"  {name:<26}{cnt / trials * 100:6.2f}%  （{cnt}/{trials}）")


def demo_recursive() -> None:
    """迭代版与递归版对照。"""
    acts = random_activities(15, horizon=30, rng=random.Random(7))
    ordered = sorted(acts, key=lambda a: (a.finish, a.start))
    it = greedy_activity_selector(acts)
    rc = greedy_recursive(ordered)
    print("\n[迭代版] " + format_schedule(it))
    print("[递归版] " + format_schedule(rc))
    same = [str(a) for a in it] == [str(a) for a in rc]
    print(f"两版本结果一致：{same}，共选中 {len(it)} 个活动")


def interactive() -> None:
    menu = """
========================================================
        活动安排问题 —— 贪心算法交互演示
========================================================
  1. 教材经典算例（含完整决策过程）
  2. 手工输入活动
  3. 随机算例：三种贪心策略与最优解对比
  4. 迭代版 / 递归版结果对照
  0. 退出
--------------------------------------------------------"""
    actions = {"1": demo_textbook, "2": demo_manual, "3": demo_random, "4": demo_recursive}
    while True:
        print(menu)
        try:
            choice = input("请选择操作：").strip()
        except EOFError:
            print("\n输入结束，退出演示。")
            return
        if choice in ("0", "q", "Q", ""):
            print("已退出。")
            return
        func = actions.get(choice)
        if func is None:
            print("无效选项，请重新输入。")
            continue
        try:
            func()
        except (ValueError, EOFError) as exc:
            print(f"输入有误：{exc}")


# ----------------------------------------------------------------------------
# 六、自动功能对拍测试
# ----------------------------------------------------------------------------
class Checker:
    """极简断言收集器：记录通过/失败条数，便于脚本化判断。"""

    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, cond: bool, name: str, detail: str = "") -> None:
        if cond:
            self.passed += 1
            print(f"  [PASS] {name}")
        else:
            self.failed += 1
            print(f"  [FAIL] {name}  {detail}")

    def summary(self) -> bool:
        total = self.passed + self.failed
        print(f"\n对拍结果：{self.passed}/{total} 通过，{self.failed} 失败")
        return self.failed == 0


def _is_feasible(chosen: Sequence[Activity]) -> bool:
    """检查解集内部两两相容，且按结束时间有序。"""
    ordered = sorted(chosen, key=lambda a: (a.finish, a.start))
    if [str(a) for a in ordered] != [str(a) for a in chosen]:
        return False
    return all(chosen[i].compatible_with(chosen[i + 1]) for i in range(len(chosen) - 1))


def run_check(seed: int = 2024) -> int:
    print("=" * 64)
    print("活动安排问题 —— 自动功能对拍测试")
    print("=" * 64)
    ck = Checker()

    # --- 用例 1：教材经典算例 ---
    print("\n[1] 教材经典算例")
    data = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9),
            (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
    acts = [Activity(i + 1, s, f, f"a{i + 1}") for i, (s, f) in enumerate(data)]
    chosen = greedy_activity_selector(acts)
    ck.check(len(chosen) == 4, "最大相容活动数 = 4", f"实际 {len(chosen)}")
    ck.check(_is_feasible(chosen), "解集两两相容且有序", format_schedule(chosen))
    ck.check([a.idx for a in chosen] == [1, 4, 8, 11], "选中活动编号为 a1,a4,a8,a11",
             str([a.idx for a in chosen]))

    # --- 用例 2：边界情形 ---
    print("\n[2] 边界情形")
    ck.check(greedy_activity_selector([]) == [], "空集合 -> 空解")
    single = [Activity(1, 2, 3)]
    ck.check(len(greedy_activity_selector(single)) == 1, "单活动 -> 选中 1 个")
    overlap = [Activity(i, 0, 10) for i in range(1, 6)]
    ck.check(len(greedy_activity_selector(overlap)) == 1, "5 个活动完全重叠 -> 仅 1 个")
    chain = [Activity(i, i, i + 1) for i in range(1, 21)]
    ck.check(len(greedy_activity_selector(chain)) == 20, "20 个首尾相接活动 -> 全选")
    same_finish = [Activity(1, 0, 5), Activity(2, 1, 5), Activity(3, 4, 5)]
    ck.check(len(greedy_activity_selector(same_finish)) == 1, "结束时间相同 -> 仅 1 个")
    touch = [Activity(1, 0, 5), Activity(2, 5, 9)]
    ck.check(len(greedy_activity_selector(touch)) == 2, "端点相接 start==finish 视为相容")

    # --- 用例 3：随机对拍（穷举，n <= 12） ---
    print("\n[3] 随机对拍：穷举 2^n 枚举 vs 贪心（n = 1..12，每个规模 200 例）")
    rng = random.Random(seed)
    bad = 0
    cases = 0
    for n in range(1, 13):
        for _ in range(200):
            a = random_activities(n, horizon=25, rng=rng)
            g = len(greedy_activity_selector(a))
            b = optimal_count_bruteforce(a)
            cases += 1
            if g != b or not _is_feasible(greedy_activity_selector(a)):
                bad += 1
                if bad <= 3:
                    print(f"    不一致：n={n} greedy={g} brute={b} "
                          f"数据={format_schedule(a)}")
    ck.check(bad == 0, f"贪心与穷举在 {cases} 个随机实例上完全一致", f"失败 {bad} 例")

    # --- 用例 4：随机对拍（动态规划，n 较大） ---
    print("\n[4] 随机对拍：动态规划 vs 贪心（n = 50..2000，共 120 例）")
    bad = 0
    cases = 0
    for n in [50, 100, 200, 500, 1000, 2000]:
        for _ in range(20):
            a = random_activities(n, horizon=max(20, n), rng=rng)
            g = len(greedy_activity_selector(a))
            d = optimal_count_dp(a)
            cases += 1
            if g != d:
                bad += 1
    ck.check(bad == 0, f"贪心与 DP 在 {cases} 个随机实例上完全一致", f"失败 {bad} 例")

    # --- 用例 5：反例——其它贪心策略确实会失效 ---
    print("\n[5] 反例：其它贪心准则不保证最优")
    found_start = found_dur = None
    for _ in range(20000):
        a = random_activities(rng.randint(4, 9), horizon=18, rng=rng)
        opt = optimal_count_dp(a)
        if found_start is None and len(alternative_greedy(a, "start")) < opt:
            found_start = (a, opt, len(alternative_greedy(a, "start")))
        if found_dur is None and len(alternative_greedy(a, "duration")) < opt:
            found_dur = (a, opt, len(alternative_greedy(a, "duration")))
        if found_start and found_dur:
            break
    if found_start:
        a, opt, got = found_start
        ck.check(got < opt, "按开始时间最早贪心存在次优反例",
                 f"{format_schedule(a)} 贪心={got} 最优={opt}")
    else:
        ck.check(False, "按开始时间最早贪心存在次优反例", "未找到反例")
    if found_dur:
        a, opt, got = found_dur
        ck.check(got < opt, "按持续时间最短贪心存在次优反例",
                 f"{format_schedule(a)} 贪心={got} 最优={opt}")
    else:
        ck.check(False, "按持续时间最短贪心存在次优反例", "未找到反例")

    # --- 用例 6：迭代版与递归版一致 ---
    print("\n[6] 迭代版与递归版等价性（300 例）")
    bad = 0
    for _ in range(300):
        a = random_activities(rng.randint(0, 30), horizon=40, rng=rng)
        it = [str(x) for x in greedy_activity_selector(a)]
        ordered = sorted(a, key=lambda x: (x.finish, x.start))
        rc = [str(x) for x in greedy_recursive(ordered)]
        if it != rc:
            bad += 1
    ck.check(bad == 0, "迭代版与递归版 300 例结果完全相同", f"失败 {bad} 例")

    # --- 用例 7：输入解析 ---
    print("\n[7] 输入解析")
    ck.check([str(a) for a in parse_activities("1 4, 3 5")] == ["a1[1, 4)", "a2[3, 5)"],
             "逗号分隔解析正确")
    ck.check([str(a) for a in parse_activities("1 4\n3 5")] == ["a1[1, 4)", "a2[3, 5)"],
             "换行分隔解析正确")
    try:
        parse_activities("1 4, 3")
        ck.check(False, "非法输入应抛异常")
    except ValueError:
        ck.check(True, "非法输入抛出 ValueError")

    ok = ck.summary()
    print("结论：" + ("全部对拍通过。" if ok else "存在失败用例，请检查实现。"))
    return 0 if ok else 1


# ----------------------------------------------------------------------------
# 七、性能测试（输出 CSV）
# ----------------------------------------------------------------------------
def run_bench(sizes: Sequence[int], repeat: int, seed: int, out_path: str) -> int:
    """
    性能测试说明：
      * 数据在计时区之外生成，避免把随机构造代价计入算法耗时；
      * 每次重复前用 shuffle 打乱同一批数据（Timsort 对已排序输入会退化为 O(n)，
        必须避免这种"作弊"），计时只包围排序与扫描；
      * 计时期间关闭 GC 自动回收，减少偶发抖动；每个规模取 repeat 次的中位数。
    """
    import gc

    print("=" * 64)
    print("活动安排问题 —— 性能测试")
    print("=" * 64)
    rng = random.Random(seed)
    rows = []
    header = ("n", "repeat", "sort_ms", "scan_ms", "total_ms", "selected", "select_ratio",
              "ns_per_elem", "dp_ms")

    print(f"{'n':>8}{'sort(ms)':>11}{'scan(ms)':>11}{'total(ms)':>12}"
          f"{'选中':>8}{'占比':>8}{'ns/元素':>11}{'DP(ms)':>10}")
    for n in sizes:
        base = random_activities(n, horizon=max(10, n), rng=rng)
        sort_ts, scan_ts, dp_ts, sel = [], [], [], []

        for _ in range(repeat):
            work = base[:]
            rng.shuffle(work)                      # 打乱不计时，避免有序输入使排序变快

            gc.disable()
            t0 = time.perf_counter()
            ordered = sorted(work, key=lambda a: (a.finish, a.start))
            t1 = time.perf_counter()

            chosen = []
            last = None
            for act in ordered:
                if last is None or act.start >= last:
                    chosen.append(act)
                    last = act.finish
            t2 = time.perf_counter()
            gc.enable()

            sort_ts.append((t1 - t0) * 1e3)
            scan_ts.append((t2 - t1) * 1e3)
            sel.append(len(chosen))

            if n <= 20000:                         # DP 规模更大时过慢，仅测中规模
                gc.disable()
                t3 = time.perf_counter()
                optimal_count_dp(base)
                dp_ts.append((time.perf_counter() - t3) * 1e3)
                gc.enable()

        sort_ms = statistics.median(sort_ts)
        scan_ms = statistics.median(scan_ts)
        total_ms = sort_ms + scan_ms
        selected = statistics.median(sel)
        rows.append({
            "n": n, "repeat": repeat,
            "sort_ms": round(sort_ms, 4), "scan_ms": round(scan_ms, 4),
            "total_ms": round(total_ms, 4), "selected": int(selected),
            "select_ratio": round(selected / n, 4),
            "ns_per_elem": round(total_ms * 1e6 / n, 2),
            "dp_ms": round(statistics.median(dp_ts), 4) if dp_ts else "",
        })
        print(f"{n:>8}{sort_ms:>11.3f}{scan_ms:>11.3f}{total_ms:>12.3f}"
              f"{int(selected):>8}{selected / n:>8.3f}{total_ms * 1e6 / n:>11.1f}"
              f"{(rows[-1]['dp_ms'] if rows[-1]['dp_ms'] != '' else '-'):>10}")

    # 用"总时间 / (n log2 n)"检验渐近阶：该比值应趋于常数
    print("\n[渐近性检验] total_ms 与 n·log2(n) 的比值"
          "（趋于常数即说明总代价为 O(n log n)）")
    import math
    for r in rows:
        ratio = r["total_ms"] / (r["n"] * math.log2(r["n"])) * 1e6
        print(f"  n={r['n']:>8}  total/(n log n) = {ratio:8.3f} ns")
    print("\n[排序与扫描的占比] 排序应主导总时间（O(n log n) 项），扫描为 O(n) 项")
    for r in rows:
        share = r["sort_ms"] / r["total_ms"] * 100
        print(f"  n={r['n']:>8}  排序占比 {share:5.1f}%  扫描占比 {100 - share:5.1f}%")

    with open(out_path, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nCSV 已写入：{os.path.abspath(out_path)}")
    print("\n[CSV 内容]")
    print(",".join(header))
    for r in rows:
        print(",".join(str(r[h]) for h in header))
    return 0


# ----------------------------------------------------------------------------
# 八、命令行入口
# ----------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="活动安排问题：贪心算法实现（交互演示 / 对拍 / 性能测试）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="示例：python '01活动安排问题.py' --bench --n 1000,5000,20000 --repeat 5",
    )
    parser.add_argument("--check", action="store_true", help="运行自动功能对拍测试")
    parser.add_argument("--bench", action="store_true", help="运行性能测试并输出 CSV")
    parser.add_argument("--n", default="1000,2000,5000,10000,20000,50000,100000,200000",
                        help="性能测试规模，逗号分隔")
    parser.add_argument("--repeat", type=int, default=3, help="每个规模重复次数，取中位数")
    parser.add_argument("--seed", type=int, default=2024, help="随机种子")
    parser.add_argument("--out", default="bench_activity.csv", help="CSV 输出路径")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.check:
        return run_check(seed=args.seed)
    if args.bench:
        sizes = [int(x) for x in args.n.replace("，", ",").split(",") if x.strip()]
        return run_bench(sizes, args.repeat, args.seed, args.out)
    interactive()
    return 0


if __name__ == "__main__":
    sys.exit(main())
