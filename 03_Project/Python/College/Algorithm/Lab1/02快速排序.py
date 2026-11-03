# -*- coding: utf-8 -*-
"""
程序名称：02快速排序.py —— 用分治法设计实现快速排序问题
作者    ：温哲睿
学号    ：2024201410
编写时间：2026-11-03
运行环境：Python 3.11（仅使用标准库，无第三方依赖）

运行方式：
    python "02快速排序.py"            交互式功能演示
    python "02快速排序.py" --check    自动功能对拍测试
    python "02快速排序.py" --bench    性能测试（输出 CSV 数据）
"""

import sys
import random
import time


# ============================================================
# 一、分治核心：划分（Partition）与快速排序
#     递归式：T(n) = T(k) + T(n-k-1) + O(n)
# ============================================================
def _partition(a, low, high, counter):
    """挖坑法划分：以 a[low] 为基准，把 <pivot 放左、>pivot 放右，返回基准最终下标。"""
    pivot = a[low]
    i, j = low, high
    while i < j:
        while i < j:
            counter[0] += 1
            if a[j] < pivot:
                break
            j -= 1
        if i < j:
            a[i] = a[j]
            i += 1
        while i < j:
            counter[0] += 1
            if a[i] > pivot:
                break
            i += 1
        if i < j:
            a[j] = a[i]
            j -= 1
    a[i] = pivot
    return i


def _choose_pivot(a, low, high, mode, rng):
    """基准选取策略：首元素 / 随机 / 三数取中。"""
    if mode == "first":
        return low
    if mode == "random":
        return rng.randint(low, high)
    if mode == "median3":
        mid = low + (high - low) // 2
        c = [(a[low], low), (a[mid], mid), (a[high], high)]
        c.sort(key=lambda t: t[0])
        return c[1][1]
    raise ValueError("unknown pivot mode: " + mode)


def _quick_sort(a, low, high, counter, mode, rng):
    """只递归处理较小区间，较大区间用循环继续，保证栈深 O(log n)。"""
    while low < high:
        p = _choose_pivot(a, low, high, mode, rng)
        if p != low:
            a[low], a[p] = a[p], a[low]
        k = _partition(a, low, high, counter)
        if k - low < high - k:
            _quick_sort(a, low, k - 1, counter, mode, rng)
            low = k + 1
        else:
            _quick_sort(a, k + 1, high, counter, mode, rng)
            high = k - 1


def quick_sort(a, mode="random", seed=2024201410):
    """
    输入：任意数组 a；mode 可取 'first' / 'random' / 'median3'
    输出：(升序排列后的新列表, 元素比较次数)
    """
    arr = list(a)
    counter = [0]
    rng = random.Random(seed)
    _quick_sort(arr, 0, len(arr) - 1, counter, mode, rng)
    return arr, counter[0]


# ============================================================
# 二、交互式功能演示
# ============================================================
def demo():
    print("=" * 66)
    print("实验二  快速排序（分治法）功能演示")
    print("=" * 66)
    try:
        raw = input("请输入待排序整数序列（空格分隔）：")
        a = [int(t) for t in raw.split()]
    except ValueError:
        print("输入格式错误，请重新运行。")
        return
    print("原始序列：", a)
    for mode in ("first", "random", "median3"):
        res, cmps = quick_sort(a, mode=mode)
        print(f"[{mode:>7}] 结果 = {res}   比较次数 = {cmps}")
    print("内置 sorted  ：", sorted(a))
    print("结果一致性：", all(quick_sort(a, m)[0] == sorted(a)
                            for m in ("first", "random", "median3")))


# ============================================================
# 三、自动对拍测试（验证正确性与鲁棒性）
# ============================================================
def self_check():
    print("case_id,description,input_a,first,random,median3,expected,passed")
    cases = [
        ([49, 38, 65, 97, 76, 13, 27, 49], "教材经典数据（含重复元素）"),
        ([1, 2, 3, 4, 5, 6, 7, 8],          "已升序（固定基准的最坏情形）"),
        ([8, 7, 6, 5, 4, 3, 2, 1],          "已逆序"),
        ([],                                  "空数组"),
        ([5],                                 "单元素"),
        ([3, 3, 3, 3, 3],                    "全部元素相等"),
        ([2, 1],                              "两元素逆序"),
    ]
    all_ok = True
    for i, (a, desc) in enumerate(cases, 1):
        expected = sorted(a)
        r = {m: quick_sort(a, mode=m)[0] for m in ("first", "random", "median3")}
        ok = all(r[m] == expected for m in r)
        all_ok &= ok
        print(f"{i},{desc},{a},{r['first']},{r['random']},{r['median3']},"
              f"{expected},{'PASS' if ok else 'FAIL'}")

    rng = random.Random(2024201410)
    for _ in range(2000):
        n = rng.randint(0, 80)
        a = [rng.randint(-1000, 1000) for _ in range(n)]
        expected = sorted(a)
        for m in ("first", "random", "median3"):
            if quick_sort(a, mode=m)[0] != expected:
                all_ok = False
                print(f"RANDOM_FAIL,mode={m},a={a}")
                break
        if not all_ok:
            break
    print(f"# 2000 组随机对拍结论：{'ALL PASS' if all_ok else 'FAILED'}")
    return all_ok


# ============================================================
# 四、性能测试：随机数据 O(n log n) 与有序数据 O(n^2) 退化对比
# ============================================================
def bench():
    rng = random.Random(2024201410)
    print("== 表1 随机数据：比较次数与耗时（mode=random）==")
    print("n,comparisons,comparisons_div_nlog2n,quicksort_ms,builtin_sorted_ms")
    for n in (1000, 10000, 100000, 500000):
        a = [rng.randint(0, 10 ** 9) for _ in range(n)]
        t0 = time.perf_counter()
        res, cmps = quick_sort(a, mode="random")
        t1 = time.perf_counter()
        builtin = sorted(a)
        t2 = time.perf_counter()
        assert res == builtin
        ratio = cmps / (n * (n.bit_length() - 1))
        print(f"{n},{cmps},{ratio:.3f},{(t1 - t0) * 1000:.1f},{(t2 - t1) * 1000:.1f}")

    print()
    print("== 表2 已升序数组：固定基准退化 vs 随机基准 ==")
    print("n,first_comparisons,random_comparisons,first_ms,random_ms")
    for n in (500, 1000, 2000, 4000):
        a = list(range(n))
        t0 = time.perf_counter()
        _, c1 = quick_sort(a, mode="first")
        t1 = time.perf_counter()
        _, c2 = quick_sort(a, mode="random")
        t2 = time.perf_counter()
        print(f"{n},{c1},{c2},{(t1 - t0) * 1000:.1f},{(t2 - t1) * 1000:.1f}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--check" in args:
        sys.exit(0 if self_check() else 1)
    elif "--bench" in args:
        bench()
    else:
        demo()

