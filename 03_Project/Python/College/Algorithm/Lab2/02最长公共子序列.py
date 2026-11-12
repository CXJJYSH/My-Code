#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
程序名称：02最长公共子序列.py  —— 最长公共子序列（LCS）问题（动态规划）
作者：温哲睿
学号：2024201410
编写时间：2026-11-10

问题：给定两个序列 X=<x1,x2,...,xm> 与 Y=<y1,y2,...,yn>，
      求它们的最长公共子序列（不要求连续，但要求相对次序一致）。

运行方式：
    python "02最长公共子序列.py"            交互式功能演示
    python "02最长公共子序列.py" --check    自动功能对拍测试
    python "02最长公共子序列.py" --bench    性能测试（输出 CSV 数据）

可选参数：
    --trials N     --check 的随机用例组数（默认 60）
    --maxn N       --bench 的最大规模（默认 2000）
    --repeat N     --bench 每个规模的重复次数（默认 3）
    --out FILE     --bench 的 CSV 输出路径（默认 bench_lcs.csv）
"""

import argparse
import csv
import os
import random
import sys
import time

INF = float("inf")
DIAG, UP, LEFT = "D", "U", "L"          # 回溯方向：左上 / 上 / 左


# ======================================================================
# 一、核心算法：动态规划求 LCS 长度与方案
# ======================================================================
def lcs_table(X, Y):
    """只求长度表 c（0 基前缀下标）。

    c[i][j] 表示 X 的前 i 个字符与 Y 的前 j 个字符的 LCS 长度。
    返回 (m+1) x (n+1) 的表 c。时间 O(mn)，空间 O(mn)。
    """
    m, n = len(X), len(Y)
    c = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        cur, pre = c[i], c[i - 1]
        xi = X[i - 1]
        for j in range(1, n + 1):
            if xi == Y[j - 1]:
                cur[j] = pre[j - 1] + 1
            elif pre[j] >= cur[j - 1]:
                cur[j] = pre[j]
            else:
                cur[j] = cur[j - 1]
    return c


def lcs_full(X, Y):
    """同时求长度表 c 与方向表 b，供回溯构造具体序列使用。

    b[i][j] = 'D' 表示 xi == yj，取自左上角；
              'U' 表示取上方 c[i-1][j]；
              'L' 表示取左方 c[i][j-1]。
    """
    m, n = len(X), len(Y)
    c = [[0] * (n + 1) for _ in range(m + 1)]
    b = [[UP] * (n + 1) for _ in range(m + 1)]
    for j in range(1, n + 1):
        b[0][j] = LEFT
    for i in range(1, m + 1):
        cur, pre, brow = c[i], c[i - 1], b[i]
        xi = X[i - 1]
        for j in range(1, n + 1):
            if xi == Y[j - 1]:
                cur[j] = pre[j - 1] + 1
                brow[j] = DIAG
            elif pre[j] >= cur[j - 1]:
                cur[j] = pre[j]
                brow[j] = UP
            else:
                cur[j] = cur[j - 1]
                brow[j] = LEFT
    return c, b


def lcs_sequence(b, X, Y):
    """由方向表 b 从右下角回溯，返回一个最长公共子序列。时间 O(m+n)。"""
    i, j = len(X), len(Y)
    out = []
    while i > 0 and j > 0:
        d = b[i][j]
        if d == DIAG:
            out.append(X[i - 1])
            i -= 1
            j -= 1
        elif d == UP:
            i -= 1
        else:
            j -= 1
    out.reverse()
    return "".join(out)


def lcs_length_1d(X, Y):
    """滚动数组版本：只保留两行，空间降到 O(min(m,n))，时间仍为 O(mn)。

    为了让空间为 O(min(m,n))，先把较短的序列作为列方向。
    """
    if len(X) < len(Y):
        X, Y = Y, X
    n = len(Y)
    pre = [0] * (n + 1)
    for i in range(1, len(X) + 1):
        cur = [0] * (n + 1)
        xi = X[i - 1]
        for j in range(1, n + 1):
            if xi == Y[j - 1]:
                cur[j] = pre[j - 1] + 1
            else:
                cur[j] = pre[j] if pre[j] >= cur[j - 1] else cur[j - 1]
        pre = cur
    return pre[n]


def is_subsequence(sub, seq):
    """判断 sub 是否为 seq 的子序列（双指针，O(len(seq))）。"""
    it = iter(seq)
    return all(ch in it for ch in sub)


# ======================================================================
# 二、对照算法：指数级暴力枚举（仅用于小规模对拍）
# ======================================================================
def brute_force_lcs(X, Y):
    """枚举 X 的全部 2^m 个子序列，逐个判断是否为 Y 的子序列。

    T(m,n) = O(2^m * n)，指数级，只适合 m <= 16 的对拍。
    """
    m = len(X)
    best = 0
    # 用二进制掩码枚举子集，掩码中 1 的位表示保留该字符
    for mask in range(1 << m):
        if bin(mask).count("1") <= best:
            continue                      # 剪枝：不可能更优
        sub = "".join(X[k] for k in range(m) if mask >> k & 1)
        if is_subsequence(sub, Y):
            best = len(sub)
    return best


def lcs_recursive(X, Y, i=None, j=None):
    """朴素递归（无记忆化）：T(m,n) = T(m-1,n) + T(m,n-1)，指数级。"""
    if i is None:
        i, j = len(X), len(Y)
    if i == 0 or j == 0:
        return 0
    if X[i - 1] == Y[j - 1]:
        return lcs_recursive(X, Y, i - 1, j - 1) + 1
    return max(lcs_recursive(X, Y, i - 1, j), lcs_recursive(X, Y, i, j - 1))


# ======================================================================
# 三、公共工具：打印二维表
# ======================================================================
def fmt_grid(title, X, Y, grid, char_mode=False):
    """打印 (m+1)x(n+1) 的表：行标为 X 的前缀，列标为 Y 的前缀。"""
    m, n = len(X), len(Y)
    print("  %s" % title)
    if n > 20 or m > 20:
        print("    （规模过大，此处不展开二维表，仅 m,n <= 20 时显示）")
        return
    head = "  %-4s %-3s" % ("", "eps")
    head += "".join("%3s" % ch for ch in Y)
    print(head)
    for i in range(m + 1):
        label = "eps" if i == 0 else " " + X[i - 1] + " "
        line = "  %-4s %-3s" % ("", label)
        for j in range(n + 1):
            v = grid[i][j]
            line += "%3s" % v
        print(line)


# ======================================================================
# 四、交互式功能演示
# ======================================================================
def solve_and_report(X, Y, show_tables=True):
    """求解并打印完整结果，返回 (LCS 长度, 一个最优 LCS)。"""
    c, b = lcs_full(X, Y)
    length = c[len(X)][len(Y)]
    seq = lcs_sequence(b, X, Y)

    print("  |X| = %d, |Y| = %d" % (len(X), len(Y)))
    print("  X = %s" % X)
    print("  Y = %s" % Y)
    print("  LCS 长度：%d" % length)
    print("  一个最长公共子序列：%s" % (seq if seq else "（空串）"))
    print("  方案校验：结果为 X 的子序列 = %s，为 Y 的子序列 = %s，长度一致 = %s"
          % (is_subsequence(seq, X), is_subsequence(seq, Y), len(seq) == length))
    # 把方案在 X、Y 中的匹配位置标出来，便于观察"相对次序一致、可不连续"
    pos_x = match_positions(seq, X)
    pos_y = match_positions(seq, Y)
    if seq:
        print("  在 X 中的下标：%s" % pos_x)
        print("  在 Y 中的下标：%s" % pos_y)

    if show_tables:
        fmt_grid("DP 表 c[i][j]（公共子序列长度）：", X, Y, c)
        fmt_grid("方向表 b[i][j]（D 左上 / U 上 / L 左）：", X, Y, b)
    return length, seq


def match_positions(sub, seq):
    """返回 sub 各字符在 seq 中贪心匹配到的下标列表。"""
    res, k = [], 0
    for ch in sub:
        while k < len(seq) and seq[k] != ch:
            k += 1
        if k < len(seq):
            res.append(k)
            k += 1
    return res


def demo_interactive():
    print("=" * 66)
    print(" 最长公共子序列问题 · 动态规划（交互式演示）")
    print("=" * 66)
    print("分别输入两个序列 X 和 Y（不含空格），例如：")
    print("    X = ABCBDAB")
    print("    Y = BDCABA")
    print("也可以在一行内用空格分隔同时给出：ABCBDAB BDCABA")
    print("输入 q 退出。")
    print("-" * 66)

    while True:
        try:
            line = input("序列 X（或 'X Y'）> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n再见。")
            return
        if line.lower() in ("q", "quit", "exit"):
            print("再见。")
            return
        if not line:
            continue
        parts = line.replace(",", " ").split()
        if len(parts) >= 2:
            X, Y = parts[0], parts[1]
        elif parts[0].isdigit():
            print("  [提示] 请输入序列（字母串），不要只输入数字。\n")
            continue
        else:
            X = parts[0]
            try:
                Y = input("序列 Y> ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n再见。")
                return
            if not Y:
                print("  [输入错误] Y 不能为空，请重新输入。\n")
                continue

        print("\n[计算结果]")
        length, seq = solve_and_report(X, Y)

        if len(X) <= 16:
            bf = brute_force_lcs(X, Y)
            print("  穷举验证：枚举 X 的 2^%d = %d 个子序列，暴力最优值 = %d，%s"
                  % (len(X), 1 << len(X), bf,
                     "与 DP 一致" if bf == length else "与 DP 不一致！"))
        one_d = lcs_length_1d(X, Y)
        print("  滚动数组版本（O(min(m,n)) 空间）：长度 = %d，%s"
              % (one_d, "与二维版本一致" if one_d == length else "不一致！"))
        print("-" * 66)


# ======================================================================
# 五、自动功能对拍测试（--check）
# ======================================================================
def run_check(trials=60, seed=2026):
    print("=" * 70)
    print(" 最长公共子序列问题 · 自动功能对拍测试")
    print("=" * 70)
    fails = 0
    total = 0

    print("\n[1/3] 固定用例")
    fixed = [
        ("教材经典用例", "ABCBDAB", "BDCABA", 4),
        ("双空串", "", "", 0),
        ("一方为空", "ABC", "", 0),
        ("完全相同", "ABCDEF", "ABCDEF", 6),
        ("无公共字符", "ABC", "DEF", 0),
        ("单字符相同", "A", "A", 1),
        ("AGGTAB/GTXTAYB", "AGGTAB", "GXTXAYB", 4),
        ("前缀关系", "ABCD", "AB", 2),
        ("重复字符", "AAAA", "AA", 2),
    ]
    for idx, (name, X, Y, expect) in enumerate(fixed, 1):
        c, b = lcs_full(X, Y)
        seq = lcs_sequence(b, X, Y)
        got = c[len(X)][len(Y)]
        ok = (got == expect and len(seq) == expect
              and is_subsequence(seq, X) and is_subsequence(seq, Y))
        total += 1
        fails += 0 if ok else 1
        print("  用例 %d：%s" % (idx, name))
        print("         X = \"%s\"，Y = \"%s\"" % (X, Y))
        print("         期望 = %-6d 实际 = %-6d 方案 = \"%s\"  结果 = %s"
              % (expect, got, seq, "PASS" if ok else "FAIL"))

    print("\n[2/3] 随机用例 %d 组（长度 0..16，与位掩码暴力枚举对拍）" % trials)
    random.seed(seed)
    alphabet = "ABCD"
    bad = 0
    for t in range(trials):
        m = random.randint(0, 16)
        n = random.randint(0, 16)
        X = "".join(random.choice(alphabet) for _ in range(m))
        Y = "".join(random.choice(alphabet) for _ in range(n))
        c, b = lcs_full(X, Y)
        seq = lcs_sequence(b, X, Y)
        got = c[len(X)][len(Y)]
        expect = brute_force_lcs(X, Y)
        one_d = lcs_length_1d(X, Y)
        ok = (got == expect and one_d == got and len(seq) == got
              and is_subsequence(seq, X) and is_subsequence(seq, Y))
        total += 1
        if not ok:
            bad += 1
            fails += 1
            print("    FAIL X=%s Y=%s DP=%d BF=%d 1D=%d 方案=%s"
                  % (X, Y, got, expect, one_d, seq))
    print("  随机对拍：%d 组，失败 %d 组。" % (trials, bad))

    print("\n[3/3] 一致性与边界")
    X, Y = "ABCBDAB", "BDCABA"
    c, b = lcs_full(X, Y)
    checks = [
        ("方向表 b 与长度表 c 一致", _check_dir_table(c, b, X, Y)),
        ("递归解与 DP 解一致", lcs_recursive("ABCBD", "ACBD") ==
            lcs_table("ABCBD", "ACBD")[5][4]),
        ("交换 X,Y 长度不变", lcs_length_1d(X, Y) == lcs_length_1d(Y, X) == 4),
        ("子序列判定函数正确", is_subsequence("BCA", "ABCBDAB") and
            not is_subsequence("CBA", "ABCDEF")),
        ("二维表尺寸为 (m+1)x(n+1)",
            len(c) == len(X) + 1 and len(c[0]) == len(Y) + 1),
    ]
    for name, ok in checks:
        total += 1
        fails += 0 if ok else 1
        print("  %s：%s" % (name, "PASS" if ok else "FAIL"))

    print("\n" + "=" * 70)
    if fails == 0:
        print(" 测试结论：全部 %d 项检查通过（PASS），DP 结果与暴力枚举完全一致。"
              % total)
    else:
        print(" 测试结论：共 %d 项检查，失败 %d 项（FAIL）。" % (total, fails))
    print("=" * 70)
    return 0 if fails == 0 else 1


def _check_dir_table(c, b, X, Y):
    """逐格验证方向表与长度表的自洽性。"""
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            d = b[i][j]
            if X[i - 1] == Y[j - 1]:
                if d != DIAG or c[i][j] != c[i - 1][j - 1] + 1:
                    return False
            else:
                best = max(c[i - 1][j], c[i][j - 1])
                if c[i][j] != best:
                    return False
                if d == UP and c[i - 1][j] < best:
                    return False
                if d == LEFT and c[i][j - 1] < best:
                    return False
    return True


# ======================================================================
# 六、性能测试（--bench）
# ======================================================================
def _time_once(fn, *args):
    t0 = time.perf_counter()
    fn(*args)
    return (time.perf_counter() - t0) * 1000.0


def run_bench(max_n=2000, repeat=3, out_path="bench_lcs.csv", seed=7):
    print("=" * 78)
    print(" 最长公共子序列问题 · 性能测试（纯 Python 实现，单线程）")
    print("=" * 78)
    sizes = [n for n in (100, 200, 400, 800, 1200, 1600, 2000) if n <= max_n]
    if not sizes or sizes[-1] != max_n:
        sizes.append(max_n)
    sizes = sorted(set(sizes))

    print("  随机序列，字母表大小 4；m = n；每规模重复 %d 次取最小值。"
          % repeat)
    print("  理论单元格数 = m*n ~ n^2")
    print("  %6s %6s %10s %12s %12s %13s %8s"
          % ("m", "n", "单元格数", "二维best(ms)", "一维best(ms)", "ns/单元格", "t/n^2"))
    print("  " + "-" * 76)

    rows = []
    random.seed(seed)
    for n in sizes:
        X = "".join(random.choice("abcd") for _ in range(n))
        Y = "".join(random.choice("abcd") for _ in range(n))
        t2d = min(_time_once(lcs_full, X, Y) for _ in range(repeat))
        t1d = min(_time_once(lcs_length_1d, X, Y) for _ in range(repeat))
        cells = n * n
        ns_per_cell = t2d * 1e6 / cells
        ratio = t2d * 1000.0 / cells          # 微秒 / 单元格
        rows.append([n, n, cells, "%.3f" % t2d, "%.3f" % t1d,
                     "%.2f" % ns_per_cell, "%.6f" % ratio])
        print("  %6d %6d %10d %12.3f %12.3f %13.2f %8.5f"
              % (n, n, cells, t2d, t1d, ns_per_cell, ratio))

    try:
        with open(out_path, "w", newline="", encoding="utf-8-sig") as fh:
            w = csv.writer(fh)
            w.writerow(["m", "n", "cells", "t2d_ms", "t1d_ms",
                        "ns_per_cell", "us_per_cell"])
            w.writerows(rows)
        print("\n  CSV 已写入：%s" % os.path.abspath(out_path))
    except OSError as err:
        print("\n  [警告] CSV 写入失败：%s" % err)

    print("  n 每扩大 2 倍，单元格数扩大 4 倍，二维版耗时约扩大 4 倍，t/n^2 基本稳定；")
    print("  一维滚动版耗时与之同阶而常数略大，但空间由 O(mn) 降为 O(min(m,n))。")
    print("=" * 78)
    return 0


# ======================================================================
# 七、入口
# ======================================================================
def main(argv=None):
    ap = argparse.ArgumentParser(
        description="最长公共子序列问题：动态规划求解 + 对拍 + 性能测试",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="运行方式：\n"
               "  python \"02最长公共子序列.py\"            交互式功能演示\n"
               "  python \"02最长公共子序列.py\" --check    自动功能对拍测试\n"
               "  python \"02最长公共子序列.py\" --bench    性能测试（输出 CSV 数据）")
    ap.add_argument("--check", action="store_true", help="自动功能对拍测试")
    ap.add_argument("--bench", action="store_true", help="性能测试并输出 CSV")
    ap.add_argument("--trials", type=int, default=60, help="--check 随机用例组数")
    ap.add_argument("--maxn", type=int, default=2000, help="--bench 最大规模 n")
    ap.add_argument("--repeat", type=int, default=3, help="--bench 每规模重复次数")
    ap.add_argument("--out", default="bench_lcs.csv", help="CSV 输出路径")
    args = ap.parse_args(argv)

    if args.check:
        return run_check(trials=args.trials)
    if args.bench:
        return run_bench(max_n=args.maxn, repeat=args.repeat, out_path=args.out)
    demo_interactive()
    return 0


if __name__ == "__main__":
    sys.exit(main())
