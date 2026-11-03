# -*- coding: utf-8 -*-
"""
程序名称：03线性时间选择.py —— 用分治法设计实现线性时间选择问题（BFPRT）
作者    ：温哲睿
学号    ：2024201410
编写时间：2026-11-03
运行环境：Python 3.11（仅使用标准库，无第三方依赖）

运行方式：
    python "03线性时间选择.py"            交互式功能演示
    python "03线性时间选择.py" --check    自动功能对拍测试
    python "03线性时间选择.py" --bench    性能测试（输出 CSV 数据）

算法要点：借助「中位数的中位数」选取好基准，保证划分后较大子问题
          规模不超过 7n/10+6，使递归式中两个子问题系数之和
          1/5 + 7/10 = 9/10 < 1，从而最坏情形时间复杂度为 O(n)。
"""

import sys
import random
import time


# ============================================================
# 一、分治核心：BFPRT 线性时间选择
# ============================================================
def _select(arr, k, deterministic, rng, stat):
    """
    在 arr 中找出第 k 小元素（k 从 1 开始计数）。
    deterministic=True 使用 BFPRT 好基准；False 使用随机基准（快速选择）。
    stat[0] 统计递归调用次数。
    """
    stat[0] += 1
    n = len(arr)
    if n <= 5:                                  # (1) 规模足够小，直接排序求解
        return sorted(arr)[k - 1]

    if deterministic:                           # (2)(3) 中位数的中位数作基准
        pivot = _median_of_medians(arr, rng, stat)
    else:
        pivot = arr[rng.randrange(n)]

    # (4) 三路划分：<pivot / ==pivot / >pivot
    left, equal, right = [], [], []
    for v in arr:
        if v < pivot:
            left.append(v)
        elif v > pivot:
            right.append(v)
        else:
            equal.append(v)
    L, E = len(left), len(equal)

    # (5) 只递归包含目标的那个子问题（减治）
    if k <= L:
        return _select(left, k, deterministic, rng, stat)
    if k <= L + E:
        return pivot
    return _select(right, k - L - E, deterministic, rng, stat)


def _median_of_medians(arr, rng, stat):
    """每 5 个元素一组取组内中位数，再递归求这些中位数的中位数。"""
    medians = []
    for i in range(0, len(arr), 5):
        group = arr[i:i + 5]
        medians.append(sorted(group)[len(group) // 2])
    return _select(medians, len(medians) // 2 + 1, True, rng, stat)


def _check_k(a, k):
    if not 1 <= k <= len(a):
        raise ValueError(f"k 越界：需满足 1 <= k <= {len(a)}，实际 k = {k}")


def bfprt_select(a, k):
    """BFPRT 选择：最坏情形 O(n)。返回第 k 小元素。"""
    _check_k(a, k)
    return _select(list(a), k, True, random.Random(2024201410), [0])


def randomized_select(a, k, seed=2024201410):
    """随机化快速选择作对照：期望 O(n)，最坏 O(n^2)。"""
    _check_k(a, k)
    return _select(list(a), k, False, random.Random(seed), [0])


def select_by_sort(a, k):
    """整体排序法作对照：O(n log n)。"""
    _check_k(a, k)
    return sorted(a)[k - 1]


# ============================================================
# 二、交互式功能演示
# ============================================================
def demo():
    print("=" * 66)
    print("实验三  线性时间选择（分治法 / BFPRT）功能演示")
    print("=" * 66)
    try:
        raw = input("请输入整数序列（空格分隔）：")
        a = [int(t) for t in raw.split()]
        k = int(input(f"请输入要查找第几小的元素 k（1~{len(a)}）："))
    except ValueError:
        print("输入格式错误，请重新运行。")
        return
    print("原始序列：", a)
    try:
        print("升序序列：", sorted(a))
        print(f"BFPRT  第 {k} 小 = {bfprt_select(a, k)}")
        print(f"随机快选 第 {k} 小 = {randomized_select(a, k)}")
        print(f"排序法   第 {k} 小 = {select_by_sort(a, k)}")
    except ValueError as e:
        print("错误：", e)


# ============================================================
# 三、自动对拍测试（验证正确性与鲁棒性）
# ============================================================
def self_check():
    print("case_id,description,input_a,k,bfprt,randomized,sort,expected,passed")
    cases = [
        ([3, 2, 1, 5, 6, 4], 2, "经典用例"),
        ([3, 2, 1, 5, 6, 4], 1, "最小值 k=1"),
        ([3, 2, 1, 5, 6, 4], 6, "最大值 k=n"),
        ([3, 2, 1, 5, 6, 4], 3, "偶数长度左中位数"),
        ([3, 2, 1, 5, 6, 4], 4, "偶数长度右中位数"),
        ([7, 7, 7, 7], 2, "全部元素相等"),
        ([5], 1, "单元素"),
        ([9, 1, 8, 2, 7, 3, 6, 4, 5, 0], 5, "长度大于 5（触发分组）"),
    ]
    all_ok = True
    for i, (a, k, desc) in enumerate(cases, 1):
        expected = sorted(a)[k - 1]
        r1, r2, r3 = bfprt_select(a, k), randomized_select(a, k), select_by_sort(a, k)
        ok = (r1 == expected and r2 == expected and r3 == expected)
        all_ok &= ok
        print(f"{i},{desc},{a},{k},{r1},{r2},{r3},{expected},{'PASS' if ok else 'FAIL'}")

    # 越界 k 必须被拒绝
    for bad_k in (0, len([1, 2, 3]) + 1):
        try:
            bfprt_select([1, 2, 3], bad_k)
            all_ok = False
            print(f"BOUNDARY_FAIL,k={bad_k} 未被拒绝")
        except ValueError:
            print(f"BOUNDARY_PASS,k={bad_k} 正确抛出异常")

    rng = random.Random(2024201410)
    for _ in range(1000):
        n = rng.randint(1, 60)
        a = [rng.randint(-100, 100) for _ in range(n)]
        k = rng.randint(1, n)
        expected = sorted(a)[k - 1]
        if bfprt_select(a, k) != expected or randomized_select(a, k) != expected:
            all_ok = False
            print(f"RANDOM_FAIL,a={a},k={k}")
            break
    print(f"# 1000 组随机对拍结论：{'ALL PASS' if all_ok else 'FAILED'}")
    return all_ok


# ============================================================
# 四、性能测试：验证 BFPRT 的线性增长趋势
# ============================================================
def bench():
    rng = random.Random(2024201410)
    print("n,k,bfprt_ms,randomized_ms,sort_ms,bfprt_result,consistent")
    for n in (1000, 10000, 100000, 300000):
        a = [rng.randint(0, 10 ** 9) for _ in range(n)]
        k = n // 2                                  # 取中位数
        t0 = time.perf_counter()
        r1 = bfprt_select(a, k)
        t1 = time.perf_counter()
        r2 = randomized_select(a, k)
        t2 = time.perf_counter()
        r3 = select_by_sort(a, k)
        t3 = time.perf_counter()
        ok = (r1 == r2 == r3 == sorted(a)[k - 1])
        print(f"{n},{k},{(t1 - t0) * 1000:.1f},{(t2 - t1) * 1000:.1f},"
              f"{(t3 - t2) * 1000:.1f},{r1},{'PASS' if ok else 'FAIL'}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--check" in args:
        sys.exit(0 if self_check() else 1)
    elif "--bench" in args:
        bench()
    else:
        demo()

