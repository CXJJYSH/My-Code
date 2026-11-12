#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
哈夫曼编码问题 —— 贪心算法

问题：给定 n 个字符及其出现频度（权值）w1, w2, ..., wn，为每个字符设计一个
      二进制前缀码（任一编码都不是另一编码的前缀），使得带权路径长度
      WPL = Σ wi · li 最小（li 为第 i 个字符的码长），即压缩效果最好。

贪心策略：把每个字符看成一棵单结点树的根，权值为其频度；每次从森林中取出
          权值最小的两棵树合并成一棵新树（新权值为二者之和）并放回森林，
          重复 n-1 次后森林中只剩一棵树，即哈夫曼树。

运行方式：
    python "02哈夫曼编码.py"            交互式功能演示
    python "02哈夫曼编码.py" --check    自动功能对拍测试
    python "02哈夫曼编码.py" --bench    性能测试（输出 CSV 数据）

--bench 可附加参数：
    --symbols 64,1024,65536   阶段一测试的符号数（逗号分隔）
    --lens 10000,200000       阶段二测试的文本长度（逗号分隔）
    --repeat 3            每个规模重复次数（取中位数）
    --seed 2024           随机数种子
    --out bench_huffman.csv   CSV 输出路径
"""

from __future__ import annotations

import argparse
import csv
import heapq
import math
import os
import random
import statistics
import string
import sys
import time
from dataclasses import dataclass, field
from functools import lru_cache
from typing import Dict, List, Optional, Sequence, Tuple


# ----------------------------------------------------------------------------
# 一、哈夫曼树结点
# ----------------------------------------------------------------------------
@dataclass
class Node:
    """哈夫曼树结点：叶子结点有 symbol，内部结点 symbol 为 None。"""

    weight: int
    symbol: Optional[str] = None
    left: Optional["Node"] = None
    right: Optional["Node"] = None
    order: int = 0          # 入堆序号，仅用于在权值相同时给出确定性的比较结果

    # heapq 在权值相同时会比较元组的第二项（order），因此不会退化为比较 Node
    def __lt__(self, other: "Node") -> bool:  # pragma: no cover - 仅作兜底
        return self.order < other.order

    @property
    def is_leaf(self) -> bool:
        return self.left is None and self.right is None


# ----------------------------------------------------------------------------
# 二、贪心算法主体：构造哈夫曼树 + 生成编码
# ----------------------------------------------------------------------------
def build_huffman_tree(freqs: Dict[str, int]) -> Optional[Node]:
    """
    用最小堆实现哈夫曼算法（贪心）。

    时间复杂度：建堆 O(n)；n-1 次合并，每次 2 次 pop + 1 次 push，均为 O(log n)
                => O(n log n)
    空间复杂度：森林最多 n 个结点 + 树的 2n-1 个结点 => O(n)

    约定：n == 1 时返回单叶结点，编码长度为 1（码字 "0"）。
    """
    if not freqs:
        return None
    heap: List[Tuple[int, int, Node]] = []
    counter = 0
    for ch, w in freqs.items():
        if w <= 0:
            raise ValueError(f"字符 {ch!r} 的频度必须为正数")
        heapq.heappush(heap, (w, counter, Node(weight=w, symbol=ch, order=counter)))
        counter += 1

    # 每次取权值最小的两个结点合并，直到只剩一个根
    while len(heap) > 1:
        w1, _, left = heapq.heappop(heap)
        w2, _, right = heapq.heappop(heap)
        parent = Node(weight=w1 + w2, symbol=None, left=left,
                      right=right, order=counter)
        counter += 1
        heapq.heappush(heap, (w1 + w2, counter, parent))

    return heap[0][2]


def build_codes(root: Optional[Node]) -> Dict[str, str]:
    """
    自顶向下遍历哈夫曼树生成编码：走左孩子记 0，走右孩子记 1。

    使用显式栈而不是递归，避免极深（退化）树的递归深度限制。
    时间复杂度 O(n)，空间 O(n)。
    """
    if root is None:
        return {}
    if root.is_leaf:                      # 只有一个字符的特殊情形
        return {root.symbol: "0"}

    codes: Dict[str, str] = {}
    stack: List[Tuple[Node, str]] = [(root, "")]
    while stack:
        node, prefix = stack.pop()
        if node.is_leaf:
            codes[node.symbol] = prefix
            continue
        if node.right is not None:
            stack.append((node.right, prefix + "1"))
        if node.left is not None:
            stack.append((node.left, prefix + "0"))
    return codes


def weighted_path_length(root: Optional[Node], depth: int = 0) -> int:
    """计算带权路径长度 WPL = Σ wi·li（递归定义，用于与编码表交叉验证）。"""
    if root is None:
        return 0
    if root.is_leaf:
        return root.weight * depth
    return (weighted_path_length(root.left, depth + 1)
            + weighted_path_length(root.right, depth + 1))


def tree_depth(root: Optional[Node]) -> int:
    """树高（最大码长），用于评估最坏情况下的解码延迟。"""
    if root is None:
        return 0
    if root.is_leaf:
        return 0
    return 1 + max(tree_depth(root.left), tree_depth(root.right))


# ----------------------------------------------------------------------------
# 三、编码 / 解码 / 度量
# ----------------------------------------------------------------------------
def encode(text: str, codes: Dict[str, str]) -> str:
    """按编码表把字符串转换为 01 位串。时间复杂度 O(总码长)。"""
    try:
        return "".join(codes[ch] for ch in text)
    except KeyError as exc:
        raise KeyError(f"字符 {exc.args[0]!r} 不在编码表中") from None


def decode(bits: str, root: Optional[Node]) -> str:
    """
    从哈夫曼树根出发逐位下行：遇 0 走左，遇 1 走右，到叶子即输出一个字符并回到根。
    时间复杂度 O(位数)；空间 O(1)（除输出串外）。
    """
    if root is None:
        return ""
    if root.is_leaf:
        return root.symbol * len(bits)

    out: List[str] = []
    node = root
    for bit in bits:
        node = node.left if bit == "0" else node.right
        if node is None:
            raise ValueError("位串非法：路径在内部结点处断开")
        if node.is_leaf:
            out.append(node.symbol)
            node = root
    if node is not root:
        raise ValueError("位串非法：结尾处没有落在叶子结点上（位串被截断）")
    return "".join(out)


def entropy(freqs: Dict[str, int]) -> float:
    """信源熵 H = -Σ pi·log2(pi)，单位为 bit/字符，是前缀码平均码长的下界。"""
    total = sum(freqs.values())
    if total == 0:
        return 0.0
    h = 0.0
    for w in freqs.values():
        if w > 0:
            p = w / total
            h -= p * math.log2(p)
    return h


def analyze(text: str, freqs: Dict[str, int], root: Node,
            codes: Dict[str, str]) -> Dict[str, float]:
    """汇总一次完整编码的各项指标，供演示与报告使用。"""
    total = sum(freqs.values())
    wpl = weighted_path_length(root)
    avg_len = wpl / total if total else 0.0
    h = entropy(freqs)
    bits = sum(len(codes[ch]) * w for ch, w in freqs.items())
    fixed_bits = (math.ceil(math.log2(len(freqs))) * total
                  if len(freqs) > 1 else total)
    return {
        "符号数": len(freqs),
        "字符总数": total,
        "WPL": wpl,
        "平均码长": avg_len,
        "熵": h,
        "编码效率": (h / avg_len) if avg_len else 0.0,
        "最小编码长度": min(len(c) for c in codes.values()) if codes else 0,
        "最大编码长度": max(len(c) for c in codes.values()) if codes else 0,
        "定长编码位数": fixed_bits,
        "哈夫曼位数": bits,
        "压缩率": bits / fixed_bits if fixed_bits else 1.0,
    }


def count_freqs(text: str) -> Dict[str, int]:
    """统计字符频度，返回按频度降序的字典（便于展示）。"""
    freqs: Dict[str, int] = {}
    for ch in text:
        freqs[ch] = freqs.get(ch, 0) + 1
    return dict(sorted(freqs.items(), key=lambda kv: (-kv[1], kv[0])))


# ----------------------------------------------------------------------------
# 四、正确性基准：暴力枚举最优前缀码代价（指数级，仅用于小规模对拍）
# ----------------------------------------------------------------------------
def optimal_cost_bruteforce(weights: Sequence[int]) -> int:
    """
    枚举"所有可能的合并顺序"求最小 WPL，作为独立基准。

    任意二叉树都可以由"反复合并两棵子树"构造，且每次合并的代价等于两棵子树
    权值之和，全部合并代价之和恰等于 WPL。因此对所有合并顺序取最小值，就得到
    真正的最优前缀码代价，与哈夫曼结果比较即可验证贪心的最优性。
    """
    if len(weights) <= 1:
        return 0

    @lru_cache(maxsize=None)
    def rec(state: Tuple[int, ...]) -> int:
        if len(state) == 1:
            return 0
        best = math.inf
        n = len(state)
        for i in range(n):
            for j in range(i + 1, n):
                merged = state[i] + state[j]
                rest = [state[k] for k in range(n) if k != i and k != j]
                rest.append(merged)
                candidate = merged + rec(tuple(sorted(rest)))
                if candidate < best:
                    best = candidate
        return best

    return rec(tuple(sorted(weights)))


# ----------------------------------------------------------------------------
# 五、校验工具
# ----------------------------------------------------------------------------
def is_prefix_free(codes: Dict[str, str]) -> bool:
    """检查编码表是否为前缀码（任意码字都不是另一码字的前缀）。"""
    items = sorted(codes.items(), key=lambda kv: len(kv[1]))
    for i, (_, ci) in enumerate(items):
        for _, cj in items[i + 1:]:
            if cj.startswith(ci):
                return False
    return True


def kraft_sum(codes: Dict[str, str]) -> float:
    """校验 Kraft 不等式：完全二叉树对应的前缀码应满足 Σ 2^(-li) = 1。"""
    return sum(2.0 ** (-len(c)) for c in codes.values())


def render_tree(root: Optional[Node], prefix: str = "", is_last: bool = True,
                is_root: bool = True, label: str = "") -> List[str]:
    """
    把哈夫曼树渲染成缩进文本（左 0 / 右 1）。

    为兼容等宽字体（终端与报告），只用 ASCII 字符绘制，避免 Unicode 制表符
    在部分字体下宽度不一致导致错位。
    """
    lines: List[str] = []
    if root is None:
        return lines
    body = f"{root.symbol!r}({root.weight})" if root.is_leaf else f"*({root.weight})"
    if is_root:
        lines.append(body)
        child_prefix = ""
    else:
        lines.append(prefix + ("`--" if is_last else "|--") + label + body)
        child_prefix = prefix + ("    " if is_last else "|   ")
    if not root.is_leaf:
        lines.extend(render_tree(root.left, child_prefix, False, False, "0 "))
        lines.extend(render_tree(root.right, child_prefix, True, False, "1 "))
    return lines


# ----------------------------------------------------------------------------
# 六、交互式演示
# ----------------------------------------------------------------------------
TEXTBOOK = {"a": 45, "b": 13, "c": 12, "d": 16, "e": 9, "f": 5}

SAMPLE_TEXT = (
    "the quick brown fox jumps over the lazy dog; "
    "pack my box with five dozen liquor jugs; "
    "how vexingly quick daft zebras jump!"
)


def _width(s: str) -> int:
    """计算字符串的显示宽度（中文/全角算 2 列），用于对齐表格。"""
    import unicodedata
    return sum(2 if unicodedata.east_asian_width(ch) in "WF" else 1 for ch in s)


def _pad(s: str, width: int, align_right: bool = False) -> str:
    gap = max(0, width - _width(s))
    return (" " * gap + s) if align_right else (s + " " * gap)


def show_table(freqs: Dict[str, int], codes: Dict[str, str], total: int) -> None:
    head = ["字符", "频度", "概率", "哈夫曼码", "码长", "贡献位数"]
    body = []
    for ch, w in freqs.items():
        body.append([repr(ch), str(w), f"{w / total:.4f}", codes[ch],
                     str(len(codes[ch])), str(len(codes[ch]) * w)])
    widths = [max(_width(head[i]), max((_width(r[i]) for r in body), default=0))
              for i in range(len(head))]
    print("  ".join(_pad(head[i], widths[i], i > 0) for i in range(len(head))))
    print("-" * (sum(widths) + 2 * (len(head) - 1)))
    for r in body:
        print("  ".join(_pad(r[i], widths[i], i > 0) for i in range(len(r))))


def demo_textbook() -> None:
    print("\n[算例] 教材经典频度表：a:45 b:13 c:12 d:16 e:9 f:5")
    root = build_huffman_tree(TEXTBOOK)
    codes = build_codes(root)
    total = sum(TEXTBOOK.values())
    show_table(TEXTBOOK, codes, total)
    print(f"\n带权路径长度 WPL = {weighted_path_length(root)}（理论最优值 224）")
    print(f"平均码长 = {weighted_path_length(root) / total:.4f} bit/字符，"
          f"熵 = {entropy(TEXTBOOK):.4f} bit/字符")
    print("哈夫曼树结构：")
    for line in render_tree(root):
        print("  " + line)
    print(f"前缀码校验：{is_prefix_free(codes)}；Kraft 和 = {kraft_sum(codes):.6f}")


def demo_manual() -> None:
    print("\n请输入字符及其频度，形如 a:45,b:13,c:12（也支持 汉字:12 的形式）")
    raw = input("频度表：").strip()
    if not raw:
        print("未输入内容，返回主菜单。")
        return
    freqs: Dict[str, int] = {}
    for item in raw.replace("，", ",").split(","):
        item = item.strip()
        if not item:
            continue
        if ":" not in item and "：" not in item:
            raise ValueError(f"无法解析 '{item}'，应形如 a:45")
        ch, w = item.replace("：", ":").split(":", 1)
        freqs[ch] = int(w)
    root = build_huffman_tree(freqs)
    codes = build_codes(root)
    total = sum(freqs.values())
    show_table(freqs, codes, total)
    print(f"\nWPL = {weighted_path_length(root)}，平均码长 = "
          f"{weighted_path_length(root) / total:.4f} bit/字符")
    print(f"前缀码校验：{is_prefix_free(codes)}；最大码长 = {tree_depth(root)}")


def demo_text_roundtrip() -> None:
    print("\n[算例] 对一段英文文本做完整编解码")
    text = SAMPLE_TEXT
    freqs = count_freqs(text)
    root = build_huffman_tree(freqs)
    codes = build_codes(root)
    bits = encode(text, codes)
    back = decode(bits, root)
    print(f"原文（{len(text)} 字符）：{text[:60]}...")
    show_table(freqs, codes, len(text))
    stats = analyze(text, freqs, root, codes)
    print(f"\n编码后位数 = {len(bits)}，定长编码需 {stats['定长编码位数']} 位，"
          f"压缩率 = {stats['压缩率'] * 100:.2f}%")
    print(f"平均码长 = {stats['平均码长']:.4f} bit，熵 = {stats['熵']:.4f} bit，"
          f"编码效率 = {stats['编码效率'] * 100:.2f}%")
    print(f"解码结果与原文一致：{back == text}")
    print(f"前 80 位码流：{bits[:80]}...")


def demo_tree() -> None:
    print("\n[算例] 小规模哈夫曼树结构可视化（8 个随机权值）")
    rng = random.Random(11)
    freqs = {str(i + 1): rng.randrange(1, 30) for i in range(8)}
    print("频度：" + "，".join(f"{k}:{v}" for k, v in freqs.items()))
    root = build_huffman_tree(freqs)
    codes = build_codes(root)
    for line in render_tree(root):
        print("  " + line)
    print("\n编码表：" + "，".join(f"{k}→{v}" for k, v in sorted(codes.items())))
    print(f"WPL = {weighted_path_length(root)}，"
          f"暴力枚举最优值 = {optimal_cost_bruteforce(list(freqs.values()))}")


def interactive() -> None:
    menu = """
========================================================
        哈夫曼编码 —— 贪心算法交互演示
========================================================
  1. 教材经典频度算例（含哈夫曼树）
  2. 手工输入字符频度
  3. 文本编码 / 解码完整流程
  4. 哈夫曼树结构可视化（8 个权值）
  0. 退出
--------------------------------------------------------"""
    actions = {"1": demo_textbook, "2": demo_manual,
               "3": demo_text_roundtrip, "4": demo_tree}
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
        except (ValueError, KeyError, EOFError) as exc:
            print(f"输入有误：{exc}")


# ----------------------------------------------------------------------------
# 七、自动功能对拍测试
# ----------------------------------------------------------------------------
class Checker:
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


def run_check(seed: int = 2024) -> int:
    print("=" * 64)
    print("哈夫曼编码 —— 自动功能对拍测试")
    print("=" * 64)
    ck = Checker()

    # --- 用例 1：教材经典算例 ---
    print("\n[1] 教材经典算例（a:45 b:13 c:12 d:16 e:9 f:5）")
    root = build_huffman_tree(TEXTBOOK)
    codes = build_codes(root)
    wpl = weighted_path_length(root)
    ck.check(wpl == 224, "WPL = 224", f"实际 {wpl}")
    ck.check(wpl == sum(len(codes[c]) * w for c, w in TEXTBOOK.items()),
             "WPL 与编码表逐项求和一致")
    ck.check(is_prefix_free(codes), "生成的是前缀码")
    ck.check(abs(kraft_sum(codes) - 1.0) < 1e-9, "Kraft 和 = 1（满二叉树）",
             f"实际 {kraft_sum(codes):.9f}")
    ck.check(codes["a"] == "0", "最高频字符 a 的码长最短（码字 0）", f"实际 {codes['a']}")
    ck.check(sorted(len(codes[c]) for c in "abcdef") == [2, 2, 2, 3, 3, 3]
             or all(len(codes[c]) <= 4 for c in "abcdef"), "码长分布合理")

    # --- 用例 2：边界情形 ---
    print("\n[2] 边界情形")
    r1 = build_huffman_tree({"x": 1})
    c1 = build_codes(r1)
    ck.check(c1 == {"x": "0"} and decode("000", r1) == "xxx",
             "单字符 -> 码字 '0'，解码正常")
    r2 = build_huffman_tree({"p": 1, "q": 1})
    c2 = build_codes(r2)
    ck.check(sorted(c2.values()) == ["0", "1"], "两字符 -> 码字 0/1", str(c2))
    r3 = build_huffman_tree({c: 7 for c in "abcd"})
    c3 = build_codes(r3)
    ck.check(is_prefix_free(c3) and abs(kraft_sum(c3) - 1.0) < 1e-9
             and tree_depth(r3) == 2, "等频度 4 符号 -> 满二叉树，码长均为 2")
    fib = {"f1": 1, "f2": 1, "f3": 2, "f4": 3, "f5": 5, "f6": 8, "f7": 13}
    rf = build_huffman_tree(fib)
    cf = build_codes(rf)
    ck.check(weighted_path_length(rf) == 78 and tree_depth(rf) == 6,
             "斐波那契频度（最不平衡）WPL=78、树高=6",
             f"WPL={weighted_path_length(rf)}, 高={tree_depth(rf)}")
    ck.check(is_prefix_free(cf), "退化树的编码仍满足前缀性质")
    ck.check(build_huffman_tree({}) is None, "空频度表 -> 空树")

    # --- 用例 3：随机对拍（暴力枚举最优合并顺序） ---
    print("\n[3] 随机对拍：贪心 WPL vs 暴力枚举最优 WPL（n = 2..7，每规模 150 例）")
    rng = random.Random(seed)
    bad_cases = 0
    total_cases = 0
    for n in range(2, 8):
        for _ in range(150):
            weights = [rng.randrange(1, 50) for _ in range(n)]
            freqs = {f"s{i}": w for i, w in enumerate(weights)}
            root = build_huffman_tree(freqs)
            greedy = weighted_path_length(root)
            best = optimal_cost_bruteforce(weights)
            total_cases += 1
            if greedy != best:
                bad_cases += 1
                if bad_cases <= 3:
                    print(f"    不一致：{weights} 贪心={greedy} 最优={best}")
    ck.check(bad_cases == 0, f"贪心 WPL 与最优值在 {total_cases} 个随机实例上完全一致",
             f"失败 {bad_cases} 例")

    # --- 用例 4：编解码往返 ---
    print("\n[4] 编解码往返一致性（400 例随机文本）")
    alphabet = string.ascii_letters + string.digits + " .,!?"
    bad = 0
    for _ in range(400):
        chars = list(alphabet)
        rng.shuffle(chars)
        chars = chars[:rng.randint(2, 20)]
        length = rng.randint(1, 200)
        text = "".join(rng.choice(chars) for _ in range(length))
        freqs = count_freqs(text)
        root = build_huffman_tree(freqs)
        codes = build_codes(root)
        try:
            if decode(encode(text, codes), root) != text:
                bad += 1
        except Exception:
            bad += 1
    ck.check(bad == 0, "400 例随机文本 decode(encode(x)) == x", f"失败 {bad} 例")

    # --- 用例 5：前缀性质与 Kraft 等式（随机规模） ---
    print("\n[5] 前缀性质与 Kraft 等式（n = 2..60，共 120 例）")
    bad_prefix = bad_kraft = 0
    for _ in range(120):
        n = rng.randint(2, 60)
        freqs = {f"c{i}": rng.randrange(1, 1000) for i in range(n)}
        codes = build_codes(build_huffman_tree(freqs))
        if not is_prefix_free(codes):
            bad_prefix += 1
        if abs(kraft_sum(codes) - 1.0) > 1e-9:
            bad_kraft += 1
    ck.check(bad_prefix == 0, "所有用例均满足前缀性质", f"失败 {bad_prefix} 例")
    ck.check(bad_kraft == 0, "所有用例均满足 Σ2^(-li)=1", f"失败 {bad_kraft} 例")

    # --- 用例 6：频率单调性（哈夫曼树的结构性质） ---
    print("\n[6] 频率—码长单调性（严格更高频的字符码长必不更长）")
    bad = 0
    for _ in range(100):
        n = rng.randint(2, 40)
        freqs = {f"c{i}": rng.randrange(1, 500) for i in range(n)}
        codes = build_codes(build_huffman_tree(freqs))
        items = list(freqs.items())
        for i in range(n):
            for j in range(n):
                # 只对频度严格不等的情形断言（等频度时码长可自由交换）
                heavier = items[i][1] > items[j][1]
                longer = len(codes[items[i][0]]) > len(codes[items[j][0]])
                if heavier and longer:
                    bad += 1
                    break
            else:
                continue
            break
    ck.check(bad == 0, "100 例中满足 f(x)>f(y) => len(x)<=len(y)", f"失败 {bad} 例")

    # --- 用例 7：非法输入 ---
    print("\n[7] 异常处理")
    try:
        build_huffman_tree({"z": 0})
        ck.check(False, "频度为 0 应抛异常")
    except ValueError:
        ck.check(True, "频度为 0 抛出 ValueError")
    root = build_huffman_tree({"a": 2, "b": 2, "c": 1})   # 位串 "1" 停在内部结点
    try:
        decode("1", root)
        ck.check(False, "截断位串应抛异常")
    except ValueError:
        ck.check(True, "截断位串抛出 ValueError")
    try:
        encode("z", build_codes(root))
        ck.check(False, "未知字符应抛异常")
    except KeyError:
        ck.check(True, "编码表外字符抛出 KeyError")

    ok = ck.summary()
    print("结论：" + ("全部对拍通过。" if ok else "存在失败用例，请检查实现。"))
    return 0 if ok else 1


# ----------------------------------------------------------------------------
# 八、性能测试（输出 CSV）
# ----------------------------------------------------------------------------
def run_bench(symbol_counts: Sequence[int], text_lens: Sequence[int], repeat: int,
              seed: int, out_path: str) -> int:
    """
    性能测试分两个阶段，共同写入一张 CSV（用 phase 列区分）：
      phase = "build"  ：固定纯随机频度，只测建树 + 生成编码表的时间，规模从
                         几十个符号到数万符号，用于验证 O(n log n) 的增长趋势；
      phase = "code"   ：固定字母表大小，测不同文本长度下的编码/解码耗时与吞吐，
                         用于观察编解码的线性行为。
    """
    print("=" * 64)
    print("哈夫曼编码 —— 性能测试")
    print("=" * 64)
    rng = random.Random(seed)
    rows = []
    header = ("phase", "symbols", "text_len", "build_tree_ms", "build_codes_ms",
              "ns_per_symbol", "encode_ms", "decode_ms", "throughput_kchar_s",
              "avg_code_len", "entropy", "efficiency", "max_code_len")

    # ---------- 阶段一：建树规模扩展性 ----------
    print("\n[阶段一] 建树 + 生成编码表的时间随符号数 n 的变化（权值随机）")
    print(f"{'符号数':>9}{'建树(ms)':>11}{'生成编码(ms)':>14}{'合计(ms)':>11}"
          f"{'ns/符号':>10}{'最大码长':>10}")
    for n in symbol_counts:
        tree_ts, code_ts = [], []
        depth = 0
        for _ in range(repeat):
            freqs = {f"s{i}": rng.randrange(1, 10 ** 6) for i in range(n)}
            t0 = time.perf_counter()
            root = build_huffman_tree(freqs)
            t1 = time.perf_counter()
            codes = build_codes(root)
            t2 = time.perf_counter()
            tree_ts.append((t1 - t0) * 1e3)
            code_ts.append((t2 - t1) * 1e3)
            depth = tree_depth(root)
            assert len(codes) == n
        tree_ms = statistics.median(tree_ts)
        code_ms = statistics.median(code_ts)
        print(f"{n:>9}{tree_ms:>11.3f}{code_ms:>14.3f}{tree_ms + code_ms:>11.3f}"
              f"{(tree_ms + code_ms) * 1e6 / n:>10.1f}{depth:>10}")
        rows.append({
            "phase": "build", "symbols": n, "text_len": 0,
            "build_tree_ms": round(tree_ms, 4), "build_codes_ms": round(code_ms, 4),
            "ns_per_symbol": round((tree_ms + code_ms) * 1e6 / n, 1),
            "encode_ms": "", "decode_ms": "", "throughput_kchar_s": "",
            "avg_code_len": "", "entropy": "", "efficiency": "",
            "max_code_len": depth,
        })

    # ---------- 阶段二：编码/解码吞吐 ----------
    print("\n[阶段二] 编码 / 解码耗时与吞吐（字母表 64 个符号，频度服从 Zipf 分布）")
    print(f"{'文本长度':>10}{'建树(ms)':>11}{'编码(ms)':>11}{'解码(ms)':>11}"
          f"{'吞吐(k字符/s)':>15}{'平均码长':>10}{'熵':>8}{'效率':>8}")
    alphabet = list(string.ascii_letters + string.digits + " .,!?")
    weights = [max(1, int(10 ** 6 / (i + 1) ** 0.9)) for i in range(len(alphabet))]
    for L in text_lens:
        tree_ts, code_ts, enc_ts, dec_ts = [], [], [], []
        avg_len = ent = eff = 0.0
        depth = 0
        for _ in range(repeat):
            text = "".join(rng.choices(alphabet, weights=weights, k=L))
            freqs = count_freqs(text)
            t0 = time.perf_counter()
            root = build_huffman_tree(freqs)
            t1 = time.perf_counter()
            codes = build_codes(root)
            t2 = time.perf_counter()
            bits = encode(text, codes)
            t3 = time.perf_counter()
            back = decode(bits, root)
            t4 = time.perf_counter()
            assert back == text, "往返结果不一致"
            tree_ts.append((t1 - t0) * 1e3)
            code_ts.append((t2 - t1) * 1e3)
            enc_ts.append((t3 - t2) * 1e3)
            dec_ts.append((t4 - t3) * 1e3)
            wpl = weighted_path_length(root)
            avg_len = wpl / sum(freqs.values())
            ent = entropy(freqs)
            eff = ent / avg_len
            depth = tree_depth(root)
        tree_ms = statistics.median(tree_ts)
        code_ms = statistics.median(code_ts)
        enc_ms = statistics.median(enc_ts)
        dec_ms = statistics.median(dec_ts)
        throughput = L / enc_ms                            # k字符/秒
        print(f"{L:>10}{tree_ms:>11.3f}{enc_ms:>11.3f}{dec_ms:>11.3f}"
              f"{throughput:>15.1f}{avg_len:>10.3f}{ent:>8.3f}{eff:>8.3f}")
        rows.append({
            "phase": "code", "symbols": len(alphabet), "text_len": L,
            "build_tree_ms": round(tree_ms, 4), "build_codes_ms": round(code_ms, 4),
            "ns_per_symbol": "",
            "encode_ms": round(enc_ms, 4), "decode_ms": round(dec_ms, 4),
            "throughput_kchar_s": round(throughput, 1),
            "avg_code_len": round(avg_len, 4), "entropy": round(ent, 4),
            "efficiency": round(eff, 4), "max_code_len": depth,
        })

    # ---------- 渐近性检验 ----------
    print("\n[渐近性检验] 建树时间 / (n·log2 n) 应随 n 增大趋于稳定（说明是 O(n log n)）")
    for r in rows:
        if r["phase"] == "build" and r["symbols"] > 1:
            n = r["symbols"]
            total = r["build_tree_ms"] + r["build_codes_ms"]
            ratio = total / (n * math.log2(n)) * 1e6
            print(f"  n={n:>7}  (建树+编码)/(n log n) = {ratio:9.3f} ns")
    print("\n[线性性检验] 编码吞吐（k字符/秒）应基本恒定，说明编码是 O(文本长度)")
    for r in rows:
        if r["phase"] == "code":
            print(f"  len={r['text_len']:>8}  encode={r['encode_ms']:>8.3f} ms  "
                  f"decode={r['decode_ms']:>8.3f} ms  "
                  f"吞吐={r['throughput_kchar_s']:>9.1f} k字符/s")

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
# 九、命令行入口
# ----------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="哈夫曼编码：贪心算法实现（交互演示 / 对拍 / 性能测试）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="示例：python '02哈夫曼编码.py' --bench --symbols 256,4096",
    )
    parser.add_argument("--check", action="store_true", help="运行自动功能对拍测试")
    parser.add_argument("--bench", action="store_true", help="运行性能测试并输出 CSV")
    parser.add_argument("--symbols", default="64,256,1024,4096,16384,65536",
                        help="阶段一测试的不同符号数，逗号分隔")
    parser.add_argument("--lens", default="10000,50000,100000,200000",
                        help="阶段二测试的文本长度，逗号分隔")
    parser.add_argument("--repeat", type=int, default=3, help="每个规模重复次数，取中位数")
    parser.add_argument("--seed", type=int, default=2024, help="随机种子")
    parser.add_argument("--out", default="bench_huffman.csv", help="CSV 输出路径")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.check:
        return run_check(seed=args.seed)
    if args.bench:
        counts = [int(x) for x in args.symbols.replace("，", ",").split(",") if x.strip()]
        lens = [int(x) for x in args.lens.replace("，", ",").split(",") if x.strip()]
        return run_bench(counts, lens, args.repeat, args.seed, args.out)
    interactive()
    return 0


if __name__ == "__main__":
    sys.exit(main())
