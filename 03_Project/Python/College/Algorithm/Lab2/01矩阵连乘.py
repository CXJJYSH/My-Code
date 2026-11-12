#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
程序名称：01矩阵连乘.py  —— 矩阵连乘问题（动态规划）
作者：温哲睿
学号：2024201410
编写时间：2026-11-10

问题：给定 n 个矩阵 A1,A2,...,An 的维数序列 p[0..n]（Ai 为 p[i-1] x p[i]），
      求完全括号化方案，使计算 A1A2...An 所需的数乘次数最少。

运行方式：
    python "01矩阵连乘.py"            交互式功能演示
    python "01矩阵连乘.py" --check    自动功能对拍测试
    python "01矩阵连乘.py" --bench    性能测试（输出 CSV 数据）

可选参数：
    --trials N     --check 的随机用例组数（默认 60）
    --maxn N       --bench 的最大规模（默认 400）
    --repeat N     --bench 每个规模的重复次数（默认 3）
    --out FILE     --bench 的 CSV 输出路径（默认 bench_matrix_chain.csv）
"""

import argparse
import csv
import os
import random
import sys
import time

INF = float("inf")


# ======================================================================
# 一、核心算法：动态规划求解矩阵连乘
# ======================================================================
def matrix_chain_order(p):
    """矩阵连乘动态规划。

    参数 p: 维数序列 [p0,p1,...,pn]，共 n 个矩阵。
    返回 (m, s)：
        m[i][j] —— 计算子链 A[i:j] 所需的最少数乘次数（1 <= i <= j <= n）
        s[i][j] —— 子链 A[i:j] 最优断点 k（在 Ak 与 A(k+1) 之间断开）
    时间复杂度 O(n^3)，空间复杂度 O(n^2)。
    """
    n = len(p) - 1
    # m、s 均使用 1 基下标，行列 0 闲置，便于与教材公式一一对应
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    # 按子链长度 length 由小到大递推，保证子问题先于父问题求解
    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = INF
            # 枚举断点 k，取代价最小者
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s


def optimal_parens(s, i, j):
    """由断点表 s 递归构造最优完全括号化方案，如 '((A1(A2A3))A4)'。"""
    if i == j:
        return "A%d" % i
    k = s[i][j]
    return "(" + optimal_parens(s, i, k) + optimal_parens(s, k + 1, j) + ")"


def eval_parens(expr, p):
    """独立解析括号化表达式并求值，返回 (行数, 列数, 数乘次数)。

    用于交叉校验：不依赖 DP 表，直接从方案串算出代价，
    若与 m[1][n] 相等，说明 s 表记录的最优方案真实可行且最优。
    """
    pos = 0

    def parse():
        nonlocal pos
        if expr[pos] == "(":
            pos += 1
            r1, c1, cost1 = parse()
            r2, c2, cost2 = parse()
            pos += 1                      # 跳过 ')'
            if c1 != r2:
                raise ValueError("维数不匹配，方案非法")
            return r1, c2, cost1 + cost2 + r1 * c1 * c2
        pos += 1                          # 跳过 'A'
        idx = 0
        while pos < len(expr) and expr[pos].isdigit():
            idx = idx * 10 + int(expr[pos])
            pos += 1
        return p[idx - 1], p[idx], 0

    return parse()


# ======================================================================
# 二、对照算法：指数级暴力枚举（仅用于小规模对拍）
# ======================================================================
def brute_force(p, i=None, j=None):
    """穷举所有加括号方式求最少数乘次数，T(n) 为卡特兰数级，只适合 n <= 10。"""
    n = len(p) - 1
    if i is None:
        i, j = 1, n
    if i == j:
        return 0
    best = INF
    for k in range(i, j):
        cur = (brute_force(p, i, k) + brute_force(p, k + 1, j)
               + p[i - 1] * p[k] * p[j])
        if cur < best:
            best = cur
    return best


def catalan(n):
    """第 n 个卡特兰数 C(n) = C(2n,n)/(n+1)。n 个矩阵的加括号方案数为 C(n-1)。"""
    c = 1
    for k in range(n):
        c = c * (2 * n - k) // (k + 1)
    return c // (n + 1)


def theory_ops(n):
    """三层循环的精确内层执行次数：sum_{len=2..n}(n-len+1)(len-1) = n(n-1)(n+1)/6。"""
    return n * (n - 1) * (n + 1) // 6


# ======================================================================
# 三、公共工具：解析输入、打印表格
# ======================================================================
def parse_dims(text):
    """把 '30 35,15 5' 之类的输入解析为整数列表。"""
    for sep in (",", "，", "、", ";", "；"):
        text = text.replace(sep, " ")
    try:
        vals = [int(tok) for tok in text.split()]
    except ValueError:
        raise ValueError("含非数字字符，只能输入正整数")
    if len(vals) < 2:
        raise ValueError("至少需要 2 个维数（即 1 个矩阵）")
    if any(v <= 0 for v in vals):
        raise ValueError("维数必须为正整数")
    return vals


def fmt_matrix(title, tab, n, limit=9):
    """以矩阵形式打印二维表（规模过大时只打印左上角 9x9 并注明）。"""
    show = min(n, limit)
    print("  %s" % title)
    if n > limit:
        print("    （n = %d 过大，仅显示前 %d 行 / 前 %d 列）" % (n, show, show))
    head = "     " + "".join("%9s" % ("j=%d" % j) for j in range(1, show + 1))
    print(head)
    for i in range(1, show + 1):
        cells = []
        for j in range(1, show + 1):
            if j < i:
                cells.append("%9s" % "-")
            else:
                cells.append("%9d" % tab[i][j])
        print("  i=%-2d" % i + "".join(cells))


def describe_matrices(p):
    n = len(p) - 1
    return "  ".join("A%d:%dx%d" % (i + 1, p[i], p[i + 1]) for i in range(n))


# ======================================================================
# 四、交互式功能演示
# ======================================================================
def solve_and_report(p, verbose=True):
    """对给定维数序列求解并打印完整结果，返回 (最少次数, 方案串)。"""
    n = len(p) - 1
    m, s = matrix_chain_order(p)
    best = m[1][n]
    plan = optimal_parens(s, 1, n)
    rows, cols, cost = eval_parens(plan, p)

    print("  矩阵个数 n = %d" % n)
    print("  各矩阵维数：%s" % describe_matrices(p))
    print("  结果矩阵维数：%d x %d" % (rows, cols))
    print("  最少数乘次数：%d" % best)
    print("  最优括号化方案：%s" % plan)
    print("  方案独立校验：按方案串直接求值 = %d 次乘法，与 DP 结果%s"
          % (cost, "一致" if cost == best else "不一致！"))

    if verbose:
        fmt_matrix("DP 表 m[i][j]（最少数乘次数）：", m, n)
        fmt_matrix("断点表 s[i][j]（最优断点 k）：", s, n)
    return best, plan


def demo_interactive():
    print("=" * 66)
    print(" 矩阵连乘问题 · 动态规划（交互式演示）")
    print("=" * 66)
    print("输入矩阵维数序列（n+1 个正整数，空格或逗号分隔），例如：")
    print("    30 35 15 5 10 20 25   表示 6 个矩阵：")
    print("    A1:30x35  A2:35x15  A3:15x5  A4:5x10  A5:10x20  A6:20x25")
    print("输入 q 退出。")
    print("-" * 66)

    while True:
        try:
            line = input("维数序列> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见。")
            return
        if line.lower() in ("q", "quit", "exit"):
            print("再见。")
            return
        if not line:
            continue
        try:
            p = parse_dims(line)
        except ValueError as err:
            print("  [输入错误] %s，请重新输入。\n" % err)
            continue

        n = len(p) - 1
        print("\n[计算结果]")
        best, plan = solve_and_report(p)

        if n <= 10:
            bf = brute_force(p)
            print("  穷举验证：%d 个矩阵共有 %d 种加括号方案，暴力枚举最优值 = %d，%s"
                  % (n, catalan(n - 1), bf, "与 DP 一致" if bf == best else "与 DP 不一致！"))
        else:
            print("  穷举验证：n = %d 时方案数为卡特兰数 C(%d) 级，已超出暴力枚举能力，略。"
                  % (n, n - 1))

        # 展示第一个断点的局部比较，直观说明"为什么不能贪心"
        if n >= 2:
            print("  第 1 层断点比较（A1...An 在 k 处断开的总代价）：")
            m, s = matrix_chain_order(p)
            for k in range(1, n):
                q = m[1][k] + m[k + 1][n] + p[0] * p[k] * p[n]
                mark = "   <== 最优" if k == s[1][n] else ""
                print("    k=%d  代价 = %d%s" % (k, q, mark))
        print("-" * 66)


def m_of(p):  # pragma: no cover - 兼容占位，正常流程不会调用
    return matrix_chain_order(p)


# ======================================================================
# 五、自动功能对拍测试（--check）
# ======================================================================
def run_check(trials=60, seed=2026):
    print("=" * 70)
    print(" 矩阵连乘问题 · 自动功能对拍测试")
    print("=" * 70)
    fails = 0
    total = 0

    # ---------- 阶段 1：固定用例 ----------
    print("\n[1/3] 固定用例")
    fixed = [
        ("教材经典 6 矩阵", [30, 35, 15, 5, 10, 20, 25], 15125),
        ("3 矩阵对比用例", [10, 100, 5, 50], 7500),
        ("单矩阵", [10, 20], 0),
        ("2 矩阵", [5, 10, 20], 1000),
        ("全 1 维数 4 矩阵", [1, 1, 1, 1, 1], 3),
        ("递减维数 5 矩阵", [50, 40, 30, 20, 10, 5], 20000),
    ]
    for idx, (name, p, expect) in enumerate(fixed, 1):
        m, s = matrix_chain_order(p)
        got = m[1][len(p) - 1]
        ok = (got == expect)
        total += 1
        fails += 0 if ok else 1
        print("  用例 %d：%s（n = %d）" % (idx, name, len(p) - 1))
        print("         p = <%s>" % ",".join(map(str, p)))
        print("         期望 = %-10d 实际 = %-10d 结果 = %s"
              % (expect, got, "PASS" if ok else "FAIL"))

    # ---------- 阶段 2：随机对拍 ----------
    print("\n[2/3] 随机用例 %d 组（n 在 1..9 之间随机，与指数级暴力枚举对拍）" % trials)
    random.seed(seed)
    bad = 0
    for t in range(trials):
        n = random.randint(1, 9)
        p = [random.randint(1, 100) for _ in range(n + 1)]
        m, s = matrix_chain_order(p)
        got = m[1][n]
        expect = brute_force(p)
        plan = optimal_parens(s, 1, n)
        _, _, cost = eval_parens(plan, p)
        ok = (got == expect) and (cost == got)
        total += 1
        if not ok:
            bad += 1
            fails += 1
            print("    FAIL p=%s DP=%d BF=%d 方案代价=%d" % (p, got, expect, cost))
    print("  随机对拍：%d 组，失败 %d 组。" % (trials, bad))

    # ---------- 阶段 3：边界与健壮性 ----------
    print("\n[3/3] 边界与健壮性")
    cases = [
        ("空维数序列被拒绝", lambda: parse_dims("")),
        ("单个维数被拒绝", lambda: parse_dims("30")),
        ("非正维数被拒绝", lambda: parse_dims("10 0 5")),
        ("非数字被拒绝", lambda: parse_dims("10 a 5")),
        ("逗号分隔可解析", lambda: parse_dims("30,35,15,5")),
        ("中文逗号可解析", lambda: parse_dims("30，35，15，5")),
    ]
    for name, fn in cases:
        try:
            value = fn()
            ok = "拒绝" not in name
            print("  %s：解析结果 %s  ---------- %s"
                  % (name, value, "PASS" if ok else "FAIL"))
        except ValueError as err:
            ok = "拒绝" in name
            print("  %s：抛出 ValueError(%s)  ---------- %s"
                  % (name, err, "PASS" if ok else "FAIL"))
        total += 1
        fails += 0 if ok else 1

    print("\n" + "=" * 70)
    if fails == 0:
        print(" 测试结论：全部 %d 项检查通过（PASS），DP 结果与暴力枚举完全一致。" % total)
    else:
        print(" 测试结论：共 %d 项检查，失败 %d 项（FAIL）。" % (total, fails))
    print("=" * 70)
    return 0 if fails == 0 else 1


# ======================================================================
# 六、性能测试（--bench）
# ======================================================================
def run_bench(max_n=400, repeat=3, out_path="bench_matrix_chain.csv", seed=7):
    print("=" * 74)
    print(" 矩阵连乘问题 · 性能测试（纯 Python 实现，单线程）")
    print("=" * 74)
    sizes = [n for n in (10, 20, 50, 100, 200, 300, 400, 500, 800) if n <= max_n]
    if not sizes or sizes[-1] != max_n:
        sizes.append(max_n)
    sizes = sorted(set(sizes))

    print("  每规模重复 %d 次取最小值；理论内层执行次数 = n(n-1)(n+1)/6 ~ n^3/6"
          % repeat)
    print("  %6s %12s %12s %14s %12s %10s"
          % ("n", "best(ms)", "mean(ms)", "理论次数", "ns/次", "t/n^3(us)"))
    print("  " + "-" * 72)

    rows = []
    random.seed(seed)
    for n in sizes:
        p = [random.randint(1, 100) for _ in range(n + 1)]
        best = INF
        tot = 0.0
        for _ in range(repeat):
            t0 = time.perf_counter()
            matrix_chain_order(p)
            dt = (time.perf_counter() - t0) * 1000.0
            best = min(best, dt)
            tot += dt
        mean = tot / repeat
        ops = theory_ops(n)
        ns_per_op = best * 1e6 / ops if ops else 0.0
        ratio = best * 1000.0 / (n ** 3)          # 微秒 / n^3
        rows.append([n, "%.3f" % best, "%.3f" % mean, ops,
                     "%.2f" % ns_per_op, "%.6f" % ratio])
        print("  %6d %12.3f %12.3f %14d %12.2f %10.6f"
              % (n, best, mean, ops, ns_per_op, ratio))

    try:
        with open(out_path, "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.writer(fh)
            w.writerow(["n", "best_ms", "mean_ms", "theory_ops",
                        "ns_per_op", "us_per_n3"])
            w.writerows(rows)
        print("\n  CSV 已写入：%s" % os.path.abspath(out_path))
    except OSError as err:
        print("\n  [警告] CSV 写入失败：%s" % err)

    print("  结论：n 每扩大 2 倍，耗时约扩大 2^3 = 8 倍；t/n^3 一栏基本稳定，")
    print("        实测曲线与 O(n^3) 理论阶一致。")
    print("=" * 74)
    return 0


# ======================================================================
# 七、入口
# ======================================================================
def main(argv=None):
    ap = argparse.ArgumentParser(
        description="矩阵连乘问题：动态规划求解 + 对拍 + 性能测试",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="运行方式：\n"
               "  python \"01矩阵连乘.py\"            交互式功能演示\n"
               "  python \"01矩阵连乘.py\" --check    自动功能对拍测试\n"
               "  python \"01矩阵连乘.py\" --bench    性能测试（输出 CSV 数据）")
    ap.add_argument("--check", action="store_true", help="自动功能对拍测试")
    ap.add_argument("--bench", action="store_true", help="性能测试并输出 CSV")
    ap.add_argument("--trials", type=int, default=60, help="--check 随机用例组数")
    ap.add_argument("--maxn", type=int, default=400, help="--bench 最大规模 n")
    ap.add_argument("--repeat", type=int, default=3, help="--bench 每规模重复次数")
    ap.add_argument("--out", default="bench_matrix_chain.csv", help="CSV 输出路径")
    args = ap.parse_args(argv)

    if args.check:
        return run_check(trials=args.trials)
    if args.bench:
        return run_bench(max_n=args.maxn, repeat=args.repeat, out_path=args.out)
    demo_interactive()
    return 0


if __name__ == "__main__":
    sys.exit(main())
