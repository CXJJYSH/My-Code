#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
0-1 背包问题 —— 分支限界法（优先队列式 / 最大上界优先）

问题：给定 n 件物品，第 i 件物品重量 w[i]、价值 v[i]，背包容量 C。
      每件物品只能整件装入或不装入（0-1 决策），求总价值最大的装法。

算法要点：
  1. 预处理：按价值密度 v[i]/w[i] 降序排列物品，使“小数背包上界”单调有效；
  2. 状态表示：搜索树结点 (level, weight, value, bound)，level 表示前 level 件已决策；
  3. 限界函数：bound = 当前价值 + 剩余容量按贪心比例装满的“小数背包”价值，
     即线性松弛问题的最优值，是整数最优解的合法上界；
  4. 剪枝：若 bound <= 当前全局最优 best，则该子树不可能更优，整枝剪掉；
  5. 搜索策略：优先队列（最大堆）按 bound 降序出队，队首 bound 已不可能改进
     best 时可直接终止 —— 这正是“优先队列式分支限界法”。

运行方式：
    python "01背包问题.py"            交互式功能演示
    python "01背包问题.py" --check    自动功能对拍测试
    python "01背包问题.py" --bench    性能测试（输出 CSV 数据）
"""

from __future__ import annotations

import argparse
import heapq
import random
import sys
import time

INF = float("inf")
EPS = 1e-9


# --------------------------------------------------------------------------- #
# 搜索树结点
# --------------------------------------------------------------------------- #
class Node:
    """分支限界搜索树上的一个结点。

    level  : 已经决策完毕的物品件数（也即下一个待决策物品的下标）
    weight : 已装入物品的总重量
    value  : 已装入物品的总价值
    bound  : 限界函数值（该子树所能达到的价值上界）
    parent : 父结点，用于回溯构造最优解的物品选取向量
    take   : 本结点相对父结点是否“装入”了第 level-1 件物品
    """

    __slots__ = ("level", "weight", "value", "bound", "parent", "take")

    def __init__(self, level, weight, value, bound=0.0, parent=None, take=None):
        self.level = level
        self.weight = weight
        self.value = value
        self.bound = bound
        self.parent = parent
        self.take = take

    def __lt__(self, other):
        return self.bound > other.bound

    def __repr__(self):
        return f"Node(level={self.level}, w={self.weight}, v={self.value}, ub={self.bound:.2f})"


# --------------------------------------------------------------------------- #
# 核心算法
# --------------------------------------------------------------------------- #
def knapsack_bb(weights, values, capacity, trace_limit=0):
    """0-1 背包问题的优先队列式分支限界法。

    参数
    ----
    weights : List[int]   每件物品的重量（非负整数）
    values  : List[int]   每件物品的价值（非负整数）
    capacity: int         背包容量
    trace_limit : int     需要记录的前若干个被扩展结点（用于演示打印）

    返回
    ----
    dict : {
        "best_value": 最优价值,
        "chosen"    : 最优解选取的物品下标（升序）,
        "expanded"  : 实际扩展（出队并生成分支）的结点数,
        "pushed"    : 入队结点总数,
        "pruned"    : 被限界函数剪掉的结点数,
        "trace"     : 前 trace_limit 个被扩展结点的信息,
    }
    """
    n = len(weights)
    capacity = max(0, int(capacity))
    if n == 0:
        # 没有物品：唯一可行解是空集
        return {"best_value": 0, "chosen": [], "expanded": 0, "pushed": 0,
                "pruned": 0, "trace": []}

    # ---- 1. 按价值密度降序排序（贪心预处理），使小数背包上界有效 ----
    order = sorted(
        range(n),
        key=lambda i: (values[i] / weights[i]) if weights[i] > 0 else INF,
        reverse=True,
    )
    w = [weights[i] for i in order]
    v = [values[i] for i in order]

    def bound(level, cur_w, cur_v):
        """小数背包上界：把 level 之后的物品按密度贪心装入，最后一件可取小数。"""
        cap = capacity - cur_w
        b = float(cur_v)
        j = level
        while j < n:
            if w[j] <= cap:
                cap -= w[j]
                b += v[j]
                j += 1
            else:
                break
        if j < n and w[j] > 0:
            b += v[j] * cap / w[j]   # 线性松弛：允许拆分最后一件物品
        return b

    # ---- 2. 初始化根结点并入队 ----
    root = Node(0, 0, 0, bound(0, 0, 0), None, None)
    counter = 0                       # 入队序号，用于堆内稳定比较
    heap = [(-root.bound, counter, root)]
    pushed = 1
    pruned = 0
    expanded = 0
    trace = []
    best_value = 0                    # 初始最优解为空集，价值 0
    best_node = None

    # ---- 3. 最大上界优先搜索 ----
    while heap:
        neg_bound, _, node = heapq.heappop(heap)

        # 限界（全局剪枝）：队首上界已无法改进当前最优解，其余结点更不可能，
        # 直接终止搜索 —— 这是优先队列式分支限界法的重要性质。
        if -neg_bound <= best_value + EPS:
            pruned += len(heap) + 1
            break

        if node.level == n:           # 叶子结点：得到一个完整可行解
            if node.value > best_value:
                best_value = node.value
                best_node = node
            continue

        expanded += 1
        if len(trace) < trace_limit:
            trace.append((expanded, node.level, node.weight, node.value, node.bound,
                          "根结点" if node.take is None else ("装入" if node.take else "不装入")))

        i = node.level

        # 分支 A —— 装入第 i 件物品（左分支）
        if node.weight + w[i] <= capacity:
            child = Node(i + 1, node.weight + w[i], node.value + v[i], 0.0, node, True)
            child.bound = bound(i + 1, child.weight, child.value)
            if child.bound > best_value + EPS:      # 限界剪枝
                counter += 1
                heapq.heappush(heap, (-child.bound, counter, child))
                pushed += 1
            else:
                pruned += 1
        else:
            pruned += 1                             # 约束剪枝：超重

        # 分支 B —— 不装入第 i 件物品（右分支）
        child = Node(i + 1, node.weight, node.value, 0.0, node, False)
        child.bound = bound(i + 1, child.weight, child.value)
        if child.bound > best_value + EPS:
            counter += 1
            heapq.heappush(heap, (-child.bound, counter, child))
            pushed += 1
        else:
            pruned += 1

    # ---- 4. 沿父指针回溯，还原最优解 ----
    chosen = []
    if best_node is not None:
        cur = best_node
        while cur.parent is not None:
            if cur.take:
                chosen.append(order[cur.level - 1])
            cur = cur.parent
        chosen.sort()

    return {
        "best_value": best_value,
        "chosen": chosen,
        "expanded": expanded,
        "pushed": pushed,
        "pruned": pruned,
        "trace": trace,
    }


# --------------------------------------------------------------------------- #
# 参考实现（仅用于对拍验证，不参与求解）
# --------------------------------------------------------------------------- #
def brute_force(weights, values, capacity):
    """位枚举暴力：O(2^n * n)，只用于小规模正确性对拍。"""
    n = len(weights)
    best_value, best_mask = 0, 0
    for mask in range(1 << n):
        tw = tv = 0
        for i in range(n):
            if mask >> i & 1:
                tw += weights[i]
                tv += values[i]
        if tw <= capacity and tv > best_value:
            best_value, best_mask = tv, mask
    return best_value, best_mask


def dp_knapsack(weights, values, capacity):
    """一维滚动数组动态规划：O(nC)，用于中规模正确性对拍。"""
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        wi, vi = weights[i], values[i]
        for c in range(capacity, wi - 1, -1):
            cand = dp[c - wi] + vi
            if cand > dp[c]:
                dp[c] = cand
    return dp[capacity]


def check_solution(weights, values, capacity, chosen, best_value):
    """校验一个解：不超重、价值一致、且与给定最优值相容。"""
    total_w = sum(weights[i] for i in chosen)
    total_v = sum(values[i] for i in chosen)
    if total_w > capacity:
        return False, f"超重 {total_w} > {capacity}"
    if total_v != best_value:
        return False, f"解的价值 {total_v} 与报告的最优值 {best_value} 不一致"
    if len(set(chosen)) != len(chosen):
        return False, "解中存在重复物品"
    return True, "ok"


# --------------------------------------------------------------------------- #
# 模式一：交互式功能演示
# --------------------------------------------------------------------------- #
def _ask(prompt, default):
    """读取一行输入；非交互环境（管道/重定向）或输入为空时返回默认值。"""
    if not sys.stdin.isatty():
        return default
    try:
        raw = input(prompt).strip()
    except EOFError:
        return default
    return raw if raw else default


def _print_case(title, weights, values, capacity, trace_limit=14):
    print("=" * 78)
    print(title)
    print("-" * 78)
    print(f"物品数 n = {len(weights)}，背包容量 C = {capacity}")
    print(f"{'物品':<6}{'重量 w':>8}{'价值 v':>8}{'密度 v/w':>12}")
    for i, (wi, vi) in enumerate(zip(weights, values)):
        print(f"{i:<6}{wi:>8}{vi:>8}{(vi / wi if wi else float('inf')):>12.3f}")

    res = knapsack_bb(weights, values, capacity, trace_limit=trace_limit)

    print("-" * 78)
    print("搜索过程（优先队列中上界最大的结点被优先扩展）：")
    print(f"{'次序':<6}{'层':<6}{'当前重':>8}{'当前值':>8}{'上界':>10}   分支")
    for e in res["trace"]:
        print(f"{e[0]:<6}{e[1]:<6}{e[2]:>8}{e[3]:>8}{e[4]:>10.2f}   {e[5]}")
    if res["expanded"] > len(res["trace"]):
        print(f"...（共扩展 {res['expanded']} 个结点，此处仅显示前 {len(res['trace'])} 个）")

    print("-" * 78)
    print(f"最优价值  : {res['best_value']}")
    print(f"选取物品  : {res['chosen']}")
    print(f"总重量    : {sum(weights[i] for i in res['chosen'])} / {capacity}")
    print(f"扩展结点  : {res['expanded']}，入队结点 {res['pushed']}，剪枝 {res['pruned']}")
    ok, msg = check_solution(weights, values, capacity, res["chosen"], res["best_value"])
    print(f"解的合法性: {'通过' if ok else '失败'}（{msg}）")
    return res


def run_demo():
    print("0-1 背包问题 · 分支限界法（优先队列式）交互式演示")

    # 演示 1：教材经典算例 n = 4
    _print_case("【演示 1】n = 4 的经典算例",
                weights=[2, 3, 4, 5], values=[3, 4, 5, 6], capacity=8)

    # 演示 2：密度排序起作用的算例（贪心不最优，分支限界仍给最优解）
    _print_case("【演示 2】贪心非最优、分支限界仍得最优解",
                weights=[10, 20, 30, 5], values=[60, 100, 120, 30], capacity=35)

    # 演示 3：性能对比（同规模下与动态规划、暴力枚举比较结果一致性）
    print("=" * 78)
    print("【演示 3】三种算法在同一随机算例上的结果对照（n = 16）")
    print("-" * 78)
    random.seed(20240521)
    weights = [random.randint(1, 20) for _ in range(16)]
    values = [random.randint(1, 30) for _ in range(16)]
    capacity = sum(weights) // 3
    res = knapsack_bb(weights, values, capacity)
    bf_value, _ = brute_force(weights, values, capacity)
    dp_value = dp_knapsack(weights, values, capacity)
    print(f"容量 C = {capacity}")
    print(f"分支限界法 : {res['best_value']:>6}   扩展结点 {res['expanded']}")
    print(f"暴力枚举   : {bf_value:>6}   （枚举 2^16 = 65536 个组合）")
    print(f"动态规划   : {dp_value:>6}   （O(nC) = {16 * capacity} 次转移）")
    print(f"三者一致   : {'是' if res['best_value'] == bf_value == dp_value else '否'}")

    # 交互输入
    print("=" * 78)
    if not sys.stdin.isatty():
        print("（非交互环境，跳过自定义算例输入；如需交互请在终端中直接运行本程序）")
        return
    print("自定义算例（直接回车使用默认值）：")
    try:
        n = int(_ask("  物品件数 n [默认 5]：", "5"))
        cap = int(_ask("  背包容量 C [默认 10]：", "10"))
    except ValueError:
        print("  输入不是整数，改用默认值 n = 5、C = 10。")
        n, cap = 5, 10
    ws, vs = [], []
    for i in range(n):
        try:
            ws.append(int(_ask(f"  第 {i} 件重量 w[{i}] [默认 2]：", "2")))
            vs.append(int(_ask(f"  第 {i} 件价值 v[{i}] [默认 3]：", "3")))
        except ValueError:
            ws.append(2)
            vs.append(3)
    _print_case("【自定义算例】", ws, vs, cap)


# --------------------------------------------------------------------------- #
# 模式二：自动功能对拍测试
# --------------------------------------------------------------------------- #
def run_check(verbose=True):
    print("0-1 背包问题 · 分支限界法自动对拍测试")
    print("-" * 78)
    passed = failed = 0
    failures = []

    def case(name, weights, values, capacity, expect=None):
        nonlocal passed, failed
        res = knapsack_bb(weights, values, capacity)
        ok, msg = check_solution(weights, values, capacity, res["chosen"], res["best_value"])
        if ok and expect is not None and res["best_value"] != expect:
            ok, msg = False, f"期望 {expect}，实际 {res['best_value']}"
        if ok:
            passed += 1
        else:
            failed += 1
            failures.append((name, msg))
            if verbose:
                print(f"[FAIL] {name}: {msg}")
        return res

    # ---- 1. 边界与固定用例 ----
    print("[1/4] 边界用例")
    case("n = 0", [], [], 10, expect=0)
    case("容量为 0", [3, 4], [5, 6], 0, expect=0)
    case("单件可装", [5], [7], 5, expect=7)
    case("单件装不下", [6], [7], 5, expect=0)
    case("恰好装满", [2, 3, 5], [2, 3, 5], 10, expect=10)
    case("全部装不下", [9, 9, 9], [1, 1, 1], 8, expect=0)
    case("零重量物品", [0, 3], [4, 5], 3, expect=9)
    case("教材经典算例", [2, 3, 4, 5], [3, 4, 5, 6], 8, expect=10)
    case("贪心非最优算例", [10, 20, 30, 5], [60, 100, 120, 30], 35, expect=190)

    # ---- 2. 小规模随机对拍（与位枚举暴力） ----
    print("[2/4] 小规模随机对拍：分支限界 vs 位枚举暴力（2000 组）")
    random.seed(1)
    for t in range(2000):
        n = random.randint(0, 10)
        ws = [random.randint(0, 15) for _ in range(n)]
        vs = [random.randint(0, 25) for _ in range(n)]
        cap = random.randint(0, 40) if n else 0
        res = knapsack_bb(ws, vs, cap)
        bf, _ = brute_force(ws, vs, cap)
        ok, msg = check_solution(ws, vs, cap, res["chosen"], res["best_value"])
        if not ok or res["best_value"] != bf:
            failed += 1
            failures.append((f"random#{t}", f"{msg}; bf={bf}, bb={res['best_value']}, "
                                            f"w={ws}, v={vs}, C={cap}"))
        else:
            passed += 1

    # ---- 3. 中规模随机对拍（与动态规划） ----
    print("[3/4] 中规模随机对拍：分支限界 vs 动态规划（300 组）")
    random.seed(2)
    for t in range(300):
        n = random.randint(1, 25)
        ws = [random.randint(1, 30) for _ in range(n)]
        vs = [random.randint(1, 50) for _ in range(n)]
        cap = random.randint(10, 200)
        res = knapsack_bb(ws, vs, cap)
        dp = dp_knapsack(ws, vs, cap)
        ok, msg = check_solution(ws, vs, cap, res["chosen"], res["best_value"])
        if not ok or res["best_value"] != dp:
            failed += 1
            failures.append((f"dp#{t}", f"{msg}; dp={dp}, bb={res['best_value']}"))
        else:
            passed += 1

    # ---- 4. 剪枝正确性：剪掉的结点确实不可能更优 ----
    print("[4/4] 剪枝一致性：与“无剪枝全枚举”在解空间上等价（200 组）")
    random.seed(3)
    for t in range(200):
        n = random.randint(1, 8)
        ws = [random.randint(1, 10) for _ in range(n)]
        vs = [random.randint(1, 10) for _ in range(n)]
        cap = random.randint(1, 25)
        res = knapsack_bb(ws, vs, cap)
        bf, mask = brute_force(ws, vs, cap)
        if res["best_value"] != bf:
            failed += 1
            failures.append((f"prune#{t}", f"bf={bf}, bb={res['best_value']}"))
        else:
            passed += 1

    print("-" * 78)
    print(f"用例总数 {passed + failed}，通过 {passed}，失败 {failed}")
    if failures:
        print("失败明细（最多显示 10 条）：")
        for name, msg in failures[:10]:
            print(f"  - {name}: {msg}")
        print("测试结果：FAILED")
        return 1
    print("测试结果：ALL PASSED")
    return 0


# --------------------------------------------------------------------------- #
# 模式三：性能测试（CSV）
# --------------------------------------------------------------------------- #
def run_bench():
    """输出 CSV：scenario,n,capacity,time_ms,nodes,best_value,dp_time_ms。

    两个场景对照：
      random     —— 重量、价值相互独立随机（价值密度差异大，上界紧、剪枝强）
      subset_sum —— 令 v[i] = w[i]（密度全部相同，上界最松，接近最坏情况）
    """
    print("scenario,n,capacity,time_ms,nodes,best_value,dp_time_ms")
    random.seed(2024)

    # ---- 场景 A：随机算例，规模可以取得较大 ----
    for n in [10, 15, 20, 25, 30, 35, 40, 50, 60, 80, 100]:
        t_bb = t_dp = 0.0
        nodes = best_val = 0
        cap = 0
        repeat = 5
        for _ in range(repeat):
            ws = [random.randint(1, 100) for _ in range(n)]
            vs = [random.randint(1, 100) for _ in range(n)]
            cap = sum(ws) // 2

            t0 = time.perf_counter()
            res = knapsack_bb(ws, vs, cap)
            t_bb += (time.perf_counter() - t0) * 1000.0

            t0 = time.perf_counter()
            dp_knapsack(ws, vs, cap)
            t_dp += (time.perf_counter() - t0) * 1000.0

            nodes += res["pushed"]
            best_val = res["best_value"]
        print(f"random,{n},{cap},{t_bb / repeat:.4f},{nodes // repeat},{best_val},"
              f"{t_dp / repeat:.4f}")

    # ---- 场景 B：子集和型困难算例，结点数呈指数增长，规模只能取到 22 ----
    for n in [10, 12, 14, 16, 18, 20, 22]:
        ws = [random.randint(1, 100) for _ in range(n)]
        vs = ws[:]
        cap = sum(ws) // 2

        t0 = time.perf_counter()
        res = knapsack_bb(ws, vs, cap)
        t_bb = (time.perf_counter() - t0) * 1000.0

        t0 = time.perf_counter()
        dp_knapsack(ws, vs, cap)
        t_dp = (time.perf_counter() - t0) * 1000.0

        print(f"subset_sum,{n},{cap},{t_bb:.4f},{res['pushed']},{res['best_value']},"
              f"{t_dp:.4f}")


# --------------------------------------------------------------------------- #
def main(argv=None):
    parser = argparse.ArgumentParser(
        description="0-1 背包问题（分支限界法）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='运行方式：\n'
               '    python "01背包问题_分支限界法.py"            交互式功能演示\n'
               '    python "01背包问题_分支限界法.py" --check    自动功能对拍测试\n'
               '    python "01背包问题_分支限界法.py" --bench    性能测试（输出 CSV 数据）\n',
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--check", action="store_true", help="自动功能对拍测试")
    group.add_argument("--bench", action="store_true", help="性能测试（输出 CSV 数据）")
    args = parser.parse_args(argv)

    if args.check:
        return run_check()
    if args.bench:
        run_bench()
        return 0
    run_demo()
    return 0


if __name__ == "__main__":
    sys.exit(main())
