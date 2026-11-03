# -*- coding: utf-8 -*-
"""
程序名称：01二分搜索.py —— 用分治法设计实现二分搜索问题
作者    ：温哲睿
学号    ：2024201410
编写时间：2026-11-03
运行环境：Python 3.11（仅使用标准库，无第三方依赖）

运行方式：
    python "01二分搜索.py"            交互式功能演示
    python "01二分搜索.py" --check    自动功能对拍测试
    python "01二分搜索.py" --bench    性能测试（输出 CSV 数据）
"""

import sys
import random
import time


# ============================================================
# 一、分治（减治）核心算法：二分搜索
#     递归式：T(n) = T(n/2) + O(1)
# ============================================================
def binary_search_recursive(a, x, low, high, counter=None):
    """
    输入：非降序数组 a，待查元素 x，当前查找区间 [low, high]
    输出：(x 的下标, 元素比较次数)；未找到时下标为 -1
    说明：采用递归形式，最直接地体现「分解—求解—合并」的分治思想
    """
    if counter is None:
        counter = [0]
    if low > high:                              # (1) 递归出口：区间为空，查找失败
        return -1, counter[0]
    mid = low + (high - low) // 2               # (2) 分解：取中点（避免 low+high 溢出）
    counter[0] += 1                             # 统计 a[mid] 与 x 的比较
    if a[mid] == x:                             # (3) 命中：子问题的解即原问题的解
        return mid, counter[0]
    elif a[mid] > x:                            # (4) 由有序性，只可能在左半区间
        return binary_search_recursive(a, x, low, mid - 1, counter)
    else:                                       # (5) 由有序性，只可能在右半区间
        return binary_search_recursive(a, x, mid + 1, high, counter)


def binary_search_iterative(a, x):
    """迭代版本：与递归版等价，辅助空间由 O(log n) 降为 O(1)。"""
    low, high, cnt = 0, len(a) - 1, 0
    while low <= high:
        mid = low + (high - low) // 2
        cnt += 1
        if a[mid] == x:
            return mid, cnt
        if a[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1, cnt


def linear_search(a, x):
    """顺序查找，作为 O(n) 的对照算法。"""
    for i, v in enumerate(a):
        if v == x:
            return i
    return -1


# ============================================================
# 二、交互式功能演示
# ============================================================
def demo():
    print("=" * 66)
    print("实验一  二分搜索（分治法）功能演示")
    print("=" * 66)
    try:
        n = int(input("请输入数组元素个数 n："))
        raw = input(f"请输入 {n} 个整数（空格分隔，允许无序，程序自动排序）：")
        a = [int(t) for t in raw.split()]
    except ValueError:
        print("输入格式错误，请重新运行。")
        return
    if len(a) != n:
        print(f"元素个数不符：期望 {n} 个，实际 {len(a)} 个。")
        return
    a.sort()
    print("排序后的数组：", a)
    try:
        x = int(input("请输入待查找元素 x："))
    except ValueError:
        print("输入格式错误，请重新运行。")
        return

    pos_r, c_r = binary_search_recursive(a, x, 0, len(a) - 1)
    pos_i, c_i = binary_search_iterative(a, x)
    pos_l = linear_search(a, x)
    print("-" * 66)
    print(f"递归二分搜索：下标 = {pos_r:>4}   元素比较次数 = {c_r}")
    print(f"迭代二分搜索：下标 = {pos_i:>4}   元素比较次数 = {c_i}")
    print(f"顺序查找对照：下标 = {pos_l:>4}   最多需要比较 {len(a)} 次")
    print(f"理论比较次数上界：floor(log2(n))+1 = {len(a).bit_length()}")
    if pos_r >= 0:
        print(f"结论：x = {x} 是数组中第 {pos_r + 1} 个元素，查找成功。")
    else:
        print(f"结论：x = {x} 不在数组中，查找失败。")


# ============================================================
# 三、自动对拍测试（验证正确性与鲁棒性）
# ============================================================
def _ok(pos, a, x):
    """判定合法的返回下标：未命中须为 -1；命中须指向值等于 x 的位置。"""
    if x not in a:
        return pos == -1
    return 0 <= pos < len(a) and a[pos] == x


def self_check():
    print("case_id,description,input_a,input_x,reference_index,recursive,iterative,passed")
    cases = [
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 7,  "命中中间元素"),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 1,  "命中首元素（下边界）"),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 19, "命中尾元素（上边界）"),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 8,  "不存在（介于两元素之间）"),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 0,  "不存在（小于最小值）"),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19], 99, "不存在（大于最大值）"),
        ([], 5,                                          "空数组"),
        ([5], 5,                                         "单元素命中"),
        ([5], 3,                                         "单元素未命中"),
        ([2, 2, 2, 2, 2, 2], 2,                        "全部重复元素"),
    ]
    all_ok = True
    for i, (a, x, desc) in enumerate(cases, 1):
        ref = a.index(x) if x in a else -1
        pr, _ = binary_search_recursive(a, x, 0, len(a) - 1)
        pi, _ = binary_search_iterative(a, x)
        ok = _ok(pr, a, x) and _ok(pi, a, x)
        all_ok &= ok
        print(f"{i},{desc},{a},{x},{ref},{pr},{pi},{'PASS' if ok else 'FAIL'}")

    rng = random.Random(2024201410)
    for _ in range(2000):
        n = rng.randint(0, 60)
        a = sorted(rng.randint(-100, 100) for _ in range(n))
        x = rng.randint(-110, 110)
        pr, _ = binary_search_recursive(a, x, 0, len(a) - 1)
        pi, _ = binary_search_iterative(a, x)
        if not (_ok(pr, a, x) and _ok(pi, a, x)):
            all_ok = False
            print(f"RANDOM_FAIL,{a},{x},{pr},{pi}")
            break
    print(f"# 2000 组随机对拍结论：{'ALL PASS' if all_ok else 'FAILED'}")
    return all_ok


# ============================================================
# 四、性能测试：验证比较次数与 log2(n) 的关系
# ============================================================
def bench():
    print("n,recursive_compare_avg,iterative_compare_avg,log2n,recursive_ns,iterative_ns")
    rng = random.Random(2024201410)
    for k in range(10, 23):
        n = 1 << k
        a = [2 * i for i in range(n)]            # 有序序列 0, 2, 4, ..., 2n-2
        rep = 20000
        targets = [rng.randint(0, 2 * n) for _ in range(rep)]
        cr = ci = 0
        t0 = time.perf_counter()
        for x in targets:
            _, c = binary_search_recursive(a, x, 0, n - 1)
            cr += c
        t1 = time.perf_counter()
        for x in targets:
            _, c = binary_search_iterative(a, x)
            ci += c
        t2 = time.perf_counter()
        rns = (t1 - t0) * 1e9 / rep
        ins = (t2 - t1) * 1e9 / rep
        print(f"{n},{cr / rep:.2f},{ci / rep:.2f},{k},{rns:.1f},{ins:.1f}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--check" in args:
        sys.exit(0 if self_check() else 1)
    elif "--bench" in args:
        bench()
    else:
        demo()

