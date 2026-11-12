# -*- coding: utf-8 -*-
"""
0-1 背包问题 —— 回溯法（Backtracking）

问题：给定 n 件物品，第 i 件重量 w[i]、价值 v[i]，背包容量 C。
      每件物品只能整件装入或不装（0-1 决策），求装入背包的最大总价值及对应方案。

算法：子集树回溯搜索 + 约束函数（可行性剪枝）+ 限界函数（最优性剪枝）
      - 约束函数：cw + w[i] <= C，超出容量则剪去该分支
      - 限界函数：当前价值 cv 加上剩余物品"分数背包"松弛上界，
                 若上界 <= 当前最优解 best，则该分支不可能改进，直接剪去
      - 预处理：物品按单位价值 v/w 降序排列，使限界函数更紧、剪枝更早

运行方式：
    python "0-1背包问题.py"            交互式功能演示
    python "0-1背包问题.py" --check    自动功能对拍测试
    python "0-1背包问题.py" --bench    性能测试（输出 CSV 数据）
"""

from __future__ import annotations

import argparse
import csv
import os
import random
import sys
import time
from bisect import bisect_right

INF = float("inf")
CSV_FILE = "bench_result.csv"


# --------------------------------------------------------------------------- #
# 一、核心算法：回溯法求解 0-1 背包
# --------------------------------------------------------------------------- #
class KnapsackBacktracking:
    """回溯法求解 0-1 背包问题。

    属性说明：
        n        物品件数
        w, v     按单位价值降序重排后的重量、价值数组
        orig     orig[i] 表示重排后第 i 件物品在原输入中的下标
        C        背包容量
        pw, pv   重量、价值的前缀和，用于 O(log n) 计算限界值
        best     当前找到的最大价值（全局最优）
        best_x   最优解向量（重排后的下标空间）
        nodes    搜索树中实际访问的结点数
        cut_cap  被约束函数剪掉的分支数
        cut_bnd  被限界函数剪掉的分支数
    """

    __slots__ = ("n", "w", "v", "orig", "C", "pw", "pv",
                 "best", "best_x", "nodes", "cut_cap", "cut_bnd", "_path")

    def __init__(self, weights, values, capacity):
        if len(weights) != len(values):
            raise ValueError("重量数组与价值数组长度不一致")
        if capacity < 0:
            raise ValueError("背包容量不能为负数")
        for x in weights:
            if x < 0:
                raise ValueError("物品重量不能为负数")

        self.n = n = len(weights)
        self.C = capacity

        # ---- 预处理：按单位价值 v/w 降序排列（零重物品视为 +∞ 排最前） ----
        def ratio(i):
            return INF if weights[i] == 0 else values[i] / weights[i]

        order = sorted(range(n), key=lambda i: (-ratio(i), -values[i], i))
        self.orig = order
        self.w = [weights[i] for i in order]
        self.v = [values[i] for i in order]

        # ---- 前缀和：pw[t] = sum(w[0:t])，便于二分定位贪心装填分界点 ----
        self.pw = [0] * (n + 1)
        self.pv = [0] * (n + 1)
        for t in range(n):
            self.pw[t + 1] = self.pw[t] + self.w[t]
            self.pv[t + 1] = self.pv[t] + self.v[t]

        self.best = -1
        self.best_x = bytearray(n)
        self.nodes = 0
        self.cut_cap = 0
        self.cut_bnd = 0

    # ------------------------------------------------------------------ #
    # 限界函数：f(i, cap) = 用物品 i..n-1 装容量 cap 的分数背包上界
    # 由于是"可分割"松弛，其值一定 >= 对应的 0-1 整数最优值，因此剪枝安全
    # ------------------------------------------------------------------ #
    def bound(self, i: int, cap: int) -> float:
        n = self.n
        if i >= n or cap <= 0:
            return 0.0
        base_w, base_v = self.pw[i], self.pv[i]
        # 找出仍然可以整件装入的最远位置 k：pw[k] - base_w <= cap
        k = bisect_right(self.pw, base_w + cap) - 1
        if k < i:
            k = i
        if k > n:
            k = n
        value = float(self.pv[k] - base_v)
        rest = cap - (self.pw[k] - base_w)
        if k < n and rest > 0 and self.w[k] > 0:
            value += rest * self.v[k] / self.w[k]      # 装入第 k 件的分数部分
        return value

    # ------------------------------------------------------------------ #
    # 贪心初始解：按单位价值从高到低装填，得到一个可行下界，
    # 使搜索一开始就有较好的 best，显著增强限界剪枝效果
    # ------------------------------------------------------------------ #
    def _greedy_seed(self):
        cw = cv = 0
        for i in range(self.n):
            if cw + self.w[i] <= self.C:
                cw += self.w[i]
                cv += self.v[i]
                self.best_x[i] = 1
        self.best = cv

    # ------------------------------------------------------------------ #
    # 深度优先搜索子集树
    #   i    当前决策到第 i 件物品
    #   cw   已装入重量
    #   cv   已获得价值
    # ------------------------------------------------------------------ #
    def _dfs(self, i: int, cw: int, cv: int):
        if i == self.n:                                  # 到达叶结点：得到一个完整方案
            if cv > self.best:
                self.best = cv
                self.best_x = bytearray(self._path)
            return

        self.nodes += 1
        wi, vi = self.w[i], self.v[i]
        path = self._path

        # 左分支：装入第 i 件（先试"装"，便于尽早拿到更好解）
        if cw + wi <= self.C:
            if cv + vi + self.bound(i + 1, self.C - cw - wi) > self.best:
                path[i] = 1
                self._dfs(i + 1, cw + wi, cv + vi)
                path[i] = 0
            else:
                self.cut_bnd += 1
        else:
            self.cut_cap += 1                            # 约束函数剪枝

        # 右分支：不装第 i 件（先用限界函数判断有无必要继续）
        if cv + self.bound(i + 1, self.C - cw) > self.best:
            path[i] = 0
            self._dfs(i + 1, cw, cv)
        else:
            self.cut_bnd += 1

    def solve(self):
        """执行搜索，返回 (最优价值, 选中的原始下标列表, 总重量, 统计字典)。"""
        if self.n == 0:
            return 0, [], 0, {"nodes": 0, "cut_cap": 0, "cut_bnd": 0}

        self._path = bytearray(self.n)
        sys.setrecursionlimit(max(1000, self.n * 4 + 200))
        self._greedy_seed()
        self._dfs(0, 0, 0)

        chosen = [self.orig[i] for i in range(self.n) if self.best_x[i]]
        chosen.sort()
        total_w = sum(self.w[i] for i in range(self.n) if self.best_x[i])
        stats = {"nodes": self.nodes, "cut_cap": self.cut_cap, "cut_bnd": self.cut_bnd}
        return self.best, chosen, total_w, stats


def knapsack_backtracking(weights, values, capacity):
    """对外接口：返回 (最优价值, 选中的原始下标列表, 统计信息)。"""
    solver = KnapsackBacktracking(weights, values, capacity)
    best, chosen, total_w, stats = solver.solve()
    stats["total_weight"] = total_w
    return best, chosen, stats


# --------------------------------------------------------------------------- #
# 二、对照算法：动态规划（用于对拍验证正确性与最优值参照）
# --------------------------------------------------------------------------- #
def knapsack_dp(weights, values, capacity):
    """0-1 背包的一维滚动数组 DP，O(nC) 时间。返回最优价值。"""
    dp = [0] * (capacity + 1)
    for wi, vi in zip(weights, values):
        if wi > capacity:
            continue
        for c in range(capacity, wi - 1, -1):
            cand = dp[c - wi] + vi
            if cand > dp[c]:
                dp[c] = cand
    return dp[capacity]


def knapsack_bruteforce(weights, values, capacity):
    """暴力枚举全部 2^n 个子集，仅用于极小规模对拍。"""
    n = len(weights)
    best = 0
    for mask in range(1 << n):
        tw = tv = 0
        for i in range(n):
            if mask >> i & 1:
                tw += weights[i]
                tv += values[i]
        if tw <= capacity and tv > best:
            best = tv
    return best


# --------------------------------------------------------------------------- #
# 三、辅助输出
# --------------------------------------------------------------------------- #
def print_solution(weights, values, capacity, best, chosen, stats, title=""):
    if title:
        print(f"\n=== {title} ===")
    print(f"物品件数 n = {len(weights)}，背包容量 C = {capacity}")
    print("-" * 62)
    print(f"{'编号':>4}{'重量':>8}{'价值':>8}{'单价 v/w':>12}{'是否装入':>10}")
    print("-" * 62)
    pick = set(chosen)
    for i, (wi, vi) in enumerate(zip(weights, values)):
        unit = "-" if wi == 0 else f"{vi / wi:>11.3f}"
        flag = "√" if i in pick else ""
        print(f"{i:>4}{wi:>8}{vi:>8}{unit:>12}{flag:>10}")
    print("-" * 62)
    print(f"最优总价值 = {best}")
    print(f"实际总重量 = {stats.get('total_weight', 0)} / {capacity}")
    print(f"选中物品编号 = {chosen}")
    print(f"搜索树访问结点数 = {stats['nodes']}，"
          f"约束剪枝 = {stats['cut_cap']}，限界剪枝 = {stats['cut_bnd']}")
    ref = knapsack_dp(weights, values, capacity)
    print(f"动态规划参照值 = {ref}（{'一致' if ref == best else '不一致！'}）")


# --------------------------------------------------------------------------- #
# 四、模式一：交互式功能演示
# --------------------------------------------------------------------------- #
SAMPLE_W = [2, 3, 4, 5, 9]
SAMPLE_V = [3, 4, 5, 8, 10]
SAMPLE_C = 20


def demo_sample():
    result = knapsack_backtracking(SAMPLE_W, SAMPLE_V, SAMPLE_C)
    print_solution(SAMPLE_W, SAMPLE_V, SAMPLE_C, *result,
                   title="内置示例（经典教材算例）")


def demo_manual():
    print("\n请按提示输入数据（直接回车表示取默认值）。")
    n_raw = input("物品件数 n（默认 4）：").strip()
    n = int(n_raw) if n_raw else 4
    weights, values = [], []
    for i in range(n):
        w_raw = input(f"  第 {i} 件重量 w[{i}]（默认 {i + 1}）：").strip()
        v_raw = input(f"  第 {i} 件价值 v[{i}]（默认 {(i + 1) * 2}）：").strip()
        weights.append(float(w_raw) if w_raw else i + 1)
        values.append(float(v_raw) if v_raw else (i + 1) * 2)
    c_raw = input("背包容量 C（默认 6）：").strip()
    capacity = float(c_raw) if c_raw else 6

    # 统一为整数，便于报告与 DP 对拍
    if all(float(x).is_integer() for x in weights + values + [capacity]):
        weights = [int(x) for x in weights]
        values = [int(x) for x in values]
        capacity = int(capacity)
    t0 = time.perf_counter()
    best, chosen, stats = knapsack_backtracking(weights, values, capacity)
    cost = (time.perf_counter() - t0) * 1000
    print_solution(weights, values, capacity, best, chosen, stats, title="手动输入算例")
    print(f"求解耗时 = {cost:.4f} ms")


def demo_random():
    n_raw = input("\n随机生成的物品件数 n（默认 8）：").strip()
    n = int(n_raw) if n_raw else 8
    seed_raw = input("随机种子（默认 2024）：").strip()
    seed = int(seed_raw) if seed_raw else 2024
    rng = random.Random(seed)
    weights = [rng.randint(1, 20) for _ in range(n)]
    values = [rng.randint(1, 30) for _ in range(n)]
    capacity = max(1, sum(weights) // 2)
    t0 = time.perf_counter()
    best, chosen, stats = knapsack_backtracking(weights, values, capacity)
    cost = (time.perf_counter() - t0) * 1000
    print_solution(weights, values, capacity, best, chosen, stats,
                   title=f"随机算例（seed={seed}）")
    print(f"求解耗时 = {cost:.4f} ms")


def run_interactive():
    bar = "=" * 62
    line = "-" * 62
    menu_lines = [
        "",
        bar,
        " 0-1 背包问题 · 回溯法 交互式演示",
        bar,
        "  1. 内置示例（经典教材算例）",
        "  2. 手动输入物品与容量",
        "  3. 随机生成算例",
        "  0. 退出",
        line,
    ]
    menu = "\n".join(menu_lines)
    while True:
        print(menu)
        try:
            choice = input("请选择操作 [0-3]：").strip()
        except EOFError:
            print("\n输入结束，退出演示。")
            return
        if choice in ("", "1"):
            demo_sample()
        elif choice == "2":
            demo_manual()
        elif choice == "3":
            demo_random()
        elif choice == "0":
            print("演示结束。")
            return
        else:
            print("无效选项，请重新输入。")


# --------------------------------------------------------------------------- #
# 五、模式二：自动功能对拍测试
# --------------------------------------------------------------------------- #
def build_test_cases():
    cases = []

    def add(name, w, v, c):
        cases.append({"name": name, "w": list(w), "v": list(v), "c": c})

    add("空物品集", [], [], 10)
    add("容量为 0", [1, 2, 3], [5, 6, 7], 0)
    add("单件全部超重", [8, 9], [10, 20], 7)
    add("单件恰好装满", [5], [9], 5)
    add("价值全为 0", [1, 2, 3], [0, 0, 0], 3)
    add("重量全为 0（全部装走）", [0, 0, 0], [4, 5, 6], 0)
    add("重复物品", [3, 3, 3, 3], [5, 5, 5, 5], 9)
    add("容量可装下全部", [1, 2, 3], [4, 5, 6], 100)
    add("教材经典算例", SAMPLE_W, SAMPLE_V, SAMPLE_C)
    add("单位价值相同", [2, 4, 6, 8], [3, 6, 9, 12], 12)
    add("极端比例（1 重 1000 价）", [1, 50, 50, 50], [1000, 60, 60, 60], 51)
    add("贪心非最优陷阱", [10, 20, 30], [60, 100, 120], 50)
    add("递减权重", [9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9], 15)
    add("小规模随机 #1", [5, 7, 3, 9, 2], [10, 13, 7, 20, 5], 15)
    add("小规模随机 #2", [4, 6, 8, 3, 7, 5], [8, 11, 15, 6, 13, 9], 18)
    add("近似全等重量", [10] * 8, [7, 9, 4, 8, 6, 5, 9, 8], 35)
    return cases


def run_check():
    print("=" * 70)
    print(" 0-1 背包问题 · 回溯法 自动功能对拍测试")
    print(" 参照算法：动态规划（n<=10 时再叠加暴力枚举双重校验）")
    print("=" * 70)
    cases = build_test_cases()
    rng = random.Random(20240501)
    for _ in range(14):                                  # 追加 14 组随机算例
        n = rng.randint(1, 12)
        w = [rng.randint(0, 15) for _ in range(n)]
        v = [rng.randint(0, 40) for _ in range(n)]
        c = rng.randint(0, 60)
        cases.append({"name": f"随机对拍 n={n}", "w": w, "v": v, "c": c})

    passed = failed = 0
    t_all = time.perf_counter()
    for k, case in enumerate(cases, 1):
        w, v, c = case["w"], case["v"], case["c"]
        best, chosen, stats = knapsack_backtracking(w, v, c)
        expect = knapsack_dp(w, v, c) if c <= 5000 else knapsack_bruteforce(w, v, c)
        if len(w) <= 10:
            expect_bf = knapsack_bruteforce(w, v, c)
            if expect_bf != expect:
                print(f"  [警告] 参照算法自校验不一致：{case['name']}")
                expect = expect_bf

        # 校验 1：价值与参照一致
        ok = best == expect
        # 校验 2：方案本身可行（重量不超限）
        tw = sum(w[i] for i in chosen)
        ok &= tw <= c
        # 校验 3：方案价值与报告的最优值一致
        ok &= sum(v[i] for i in chosen) == best
        # 校验 4：解向量合法（下标不重复、不越界）
        ok &= len(set(chosen)) == len(chosen) and all(0 <= i < len(w) for i in chosen)

        if ok:
            passed += 1
            pruned = stats["cut_cap"] + stats["cut_bnd"]
            print(f"[{k:>2}/{len(cases)}] {case['name']:<24} PASS  "
                  f"best={best:<5} 结点={stats['nodes']:<5} 剪枝={pruned}")
        else:
            failed += 1
            print(f"[{k:>2}/{len(cases)}] {case['name']:<24} FAIL  "
                  f"got={best} expect={expect} chosen={chosen}")

    cost = (time.perf_counter() - t_all) * 1000
    print("-" * 70)
    print(f"合计 {len(cases)} 组用例：通过 {passed} 组，失败 {failed} 组，"
          f"总耗时 {cost:.2f} ms")
    print("结论：" + ("全部用例通过，回溯法结果与动态规划/暴力枚举完全一致。"
                    if failed == 0 else "存在失败用例，请检查算法实现！"))
    print("=" * 70)
    return 0 if failed == 0 else 1


# --------------------------------------------------------------------------- #
# 六、模式三：性能测试（输出 CSV）
# --------------------------------------------------------------------------- #
def run_bench(csv_path=CSV_FILE):
    """构造两组不同"区分度"的数据，观察剪枝强度对搜索量的影响。

    贴紧型：所有物品同重同值（w=7, v=11），容量取 7·n/2 附近的非整数倍，
            分数背包上界几乎恒大于整数最优值，约束/限界剪枝都难以生效，
            搜索量逼近最坏情况 2^n，用于验证 O(n·2^n) 的时间复杂度上界。
    差异型：重量、价值在 [1,50] 内均匀随机，单位价值差异大，
            限界函数紧、贪心初始解好，实际搜索量远小于 2^n。
    """
    sizes = [10, 12, 14, 16, 18, 20, 22, 24]
    repeats = 3

    def make_case(family, n, r):
        rng = random.Random(1007 * n + r)
        if family == "贴紧型":
            w = [7] * n
            v = [11] * n
            cap = 7 * n // 2 - 3
        else:
            w = [rng.randint(1, 50) for _ in range(n)]
            v = [rng.randint(1, 50) for _ in range(n)]
            cap = max(1, sum(w) // 2)
        return w, v, cap

    print("=" * 82)
    print(" 0-1 背包问题 · 回溯法 性能测试")
    print(f" 每个规模重复 {repeats} 次，结点数取平均、耗时取最小值；求解结果均与动态规划对拍")
    print("=" * 82)
    print(f"{'n':>4}{'用例族':>8}{'容量':>7}{'最优值':>8}{'结点数(均)':>13}"
          f"{'耗时ms(均)':>14}{'最小ms':>11}{'DP耗时ms':>11}")
    print("-" * 82)

    rows = []
    t_start = time.perf_counter()
    for family in ("贴紧型", "差异型"):
        for n in sizes:
            nodes_sum = 0
            time_sum = 0.0
            time_min = INF
            dp_time = 0.0
            best_val = cap = 0
            for r in range(repeats):
                w, v, cap = make_case(family, n, r)
                t0 = time.perf_counter()
                best, chosen, stats = knapsack_backtracking(w, v, cap)
                dt = (time.perf_counter() - t0) * 1000
                t1 = time.perf_counter()
                ref = knapsack_dp(w, v, cap)
                dp_time += (time.perf_counter() - t1) * 1000
                if ref != best:
                    raise AssertionError(f"结果错误：n={n} family={family} {best} != {ref}")
                nodes_sum += stats["nodes"]
                time_sum += dt
                time_min = min(time_min, dt)
                best_val = best
            avg_nodes = nodes_sum / repeats
            avg_time = time_sum / repeats
            dp_time /= repeats
            rows.append([n, family, cap, best_val, int(avg_nodes),
                         round(avg_time, 4), round(time_min, 4), round(dp_time, 4)])
            print(f"{n:>4}{family:>8}{cap:>7}{best_val:>8}{avg_nodes:>13.1f}"
                  f"{avg_time:>14.4f}{time_min:>11.4f}{dp_time:>11.4f}")

    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        wr = csv.writer(f)
        wr.writerow(["n", "family", "capacity", "best_value", "avg_nodes",
                     "avg_time_ms", "min_time_ms", "dp_time_ms"])
        wr.writerows(rows)
    print("-" * 82)
    print(f"总耗时 {(time.perf_counter() - t_start):.2f} s")
    print(f"CSV 数据已写入：{os.path.abspath(csv_path)}")
    print("=" * 82)
    return 0


# --------------------------------------------------------------------------- #
def main(argv=None):
    parser = argparse.ArgumentParser(
        description="0-1 背包问题：回溯法实现（约束函数 + 限界函数剪枝）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="运行方式：\n"
               '  python "0-1背包问题.py"            交互式功能演示\n'
               '  python "0-1背包问题.py" --check    自动功能对拍测试\n'
               '  python "0-1背包问题.py" --bench    性能测试（输出 CSV 数据）')
    parser.add_argument("--check", action="store_true", help="自动功能对拍测试")
    parser.add_argument("--bench", action="store_true", help="性能测试并输出 CSV")
    args = parser.parse_args(argv)

    if args.check:
        return run_check()
    if args.bench:
        return run_bench()
    run_interactive()
    return 0


if __name__ == "__main__":
    sys.exit(main())
