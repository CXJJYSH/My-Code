#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
单源最短路径问题 —— 分支限界法（优先队列式 / 最小距离优先）

问题：给定带权有向图 G = (V, E)，每条边 (u, v) 权 w(u, v) >= 0，给定源点 s，
      求 s 到其余每个顶点的最短路径长度及路径本身。

算法要点：
  1. 解空间：一条“从源点出发的路径”就是一个部分解，扩展方式是沿出边延伸一步；
  2. 结点状态：(dist, 当前顶点 v, 父顶点 parent)，dist 为源点到 v 的这条路径长度；
  3. 限界函数：dist 本身即该路径长度的下界估计，同时用数组 dist[] 记录“已知最短路”，
     若新路径长度不优于已知值，则该子结点不可能引出更优解，剪去；
  4. 剪枝规则：
       (a) 约束/限界剪枝： dist[u] + w(u,v) >= dist[v] 时不生成子结点；
       (b) 已确定剪枝：   顶点 v 的最短距离一旦出队确定（settled），不再扩展；
       (c) 重复结点剪枝： 同一顶点在队列中的旧、劣结点出队时直接丢弃；
  5. 搜索策略：最小堆按 dist 升序出队，队首即当前距离最小的活结点 —— 它一旦出队，
     其 dist 就是最终最短距离（要求边权非负），因此每个顶点只需出队一次。

运行方式：
    python "02单源最短路径.py"            交互式功能演示
    python "02单源最短路径.py" --check    自动功能对拍测试
    python "02单源最短路径.py" --bench    性能测试（输出 CSV 数据）
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
# 图的基本工具
# --------------------------------------------------------------------------- #
def build_adj(n, edges):
    """由边表构造邻接表。edges 中每项为 (u, v, w)，允许重边与自环。"""
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
    return adj


def check_negative(edges):
    """分支限界法（按距离最小优先）要求边权非负，否则“出队即定稿”不成立。"""
    for u, v, w in edges:
        if w < 0:
            raise ValueError(
                f"边 ({u}, {v}) 的权为 {w} < 0：优先队列式分支限界法要求边权非负，"
                f"负权图请改用 Bellman-Ford 或 SPFA 算法。"
            )


# --------------------------------------------------------------------------- #
# 核心算法
# --------------------------------------------------------------------------- #
def shortest_path_bb(n, edges, source, trace_limit=0):
    """单源最短路径的优先队列式分支限界法。

    返回
    ----
    dict : {
        "dist"    : 长度 n 的最短距离数组（不可达为 inf）,
        "prev"    : 长度 n 的前驱数组（-1 表示不可达或源点）,
        "settled" : 出队并确定最短距离的顶点数,
        "pushed"  : 入队（生成）的结点总数,
        "pruned"  : 被剪枝丢弃的结点数,
        "relax"   : 成功松弛（更新 dist）的次数,
        "trace"   : 前 trace_limit 个扩展结点的信息,
    }
    """
    check_negative(edges)
    adj = build_adj(n, edges)

    dist = [INF] * n
    prev = [-1] * n
    done = [False] * n

    dist[source] = 0
    counter = 0                                   # 入队序号，保证堆内比较稳定
    heap = [(0.0, counter, source, -1)]
    pushed = 1
    pruned = 0
    settled = 0
    relax = 0
    trace = []

    while heap:
        d, _, u, parent = heapq.heappop(heap)

        # 剪枝 (c)：同一顶点的旧结点（其 dist 已被更优值取代）直接丢弃
        if done[u]:
            pruned += 1
            continue

        # 出队即定稿：队首是当前距离最小的活结点，其 dist 已是最终最短距离
        done[u] = True
        dist[u] = d
        prev[u] = parent
        settled += 1

        relax_here = 0
        for v, w in adj[u]:
            # 剪枝 (b)：已确定最短距离的顶点不再作为扩展目标
            if done[v]:
                pruned += 1
                continue
            nd = d + w
            # 剪枝 (a)：限界 —— 新路径不优于已知最短距离，子结点无意义
            if nd < dist[v] - EPS:
                dist[v] = nd
                relax += 1
                relax_here += 1
                counter += 1
                heapq.heappush(heap, (nd, counter, v, u))
                pushed += 1
            else:
                pruned += 1

        if len(trace) < trace_limit:
            trace.append((settled, u, d, parent, relax_here))

    return {
        "dist": dist,
        "prev": prev,
        "settled": settled,
        "pushed": pushed,
        "pruned": pruned,
        "relax": relax,
        "trace": trace,
    }


def build_path(prev, source, target):
    """由前驱数组回溯 source -> target 的路径；不可达返回 None。"""
    if prev[target] == -1 and target != source:
        return None
    path = []
    cur = target
    guard = 0
    while cur != -1:
        path.append(cur)
        if cur == source:
            break
        cur = prev[cur]
        guard += 1
        if guard > len(prev) + 1:       # 防御性检查：不应出现环
            return None
    path.reverse()
    return path


def path_length(path, adj_map):
    """按邻接表（取两顶点间最小边权）累加路径长度。"""
    total = 0
    for a, b in zip(path, path[1:]):
        total += adj_map[(a, b)]
    return total


# --------------------------------------------------------------------------- #
# 参考实现（仅用于对拍验证）
# --------------------------------------------------------------------------- #
def floyd(n, edges):
    """Floyd-Warshall：O(n^3)，给出全源最短路径，作为对拍基准。"""
    D = [[INF] * n for _ in range(n)]
    for i in range(n):
        D[i][i] = 0
    for u, v, w in edges:
        if w < D[u][v]:
            D[u][v] = w
    for k in range(n):
        Dk = D[k]
        for i in range(n):
            dik = D[i][k]
            if dik == INF:
                continue
            Di = D[i]
            for j in range(n):
                nd = dik + Dk[j]
                if nd < Di[j]:
                    Di[j] = nd
    return D


def bellman_ford(n, edges, source):
    """Bellman-Ford：O(nm)，作为稀疏图上更独立的一份基准实现。"""
    dist = [INF] * n
    dist[source] = 0
    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v] - EPS:
                dist[v] = dist[u] + w
                changed = True
        if not changed:
            break
    return dist


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


def make_adj_map(edges):
    """把边表压缩成 (u, v) -> 最小边权 的字典，便于校验路径长度。"""
    m = {}
    for u, v, w in edges:
        if (u, v) not in m or w < m[(u, v)]:
            m[(u, v)] = w
    return m


def _print_case(title, n, edges, source, trace_limit=12):
    print("=" * 78)
    print(title)
    print("-" * 78)
    print(f"顶点数 |V| = {n}，边数 |E| = {len(edges)}，源点 s = {source}")
    print("边表：" + "，".join(f"{u}->{v}({w})" for u, v, w in edges))

    res = shortest_path_bb(n, edges, source, trace_limit=trace_limit)

    print("-" * 78)
    print("搜索过程（最小堆中距离最小的活结点优先出队，出队即定稿）：")
    print(f"{'次序':<6}{'顶点':<6}{'最短距离':>10}{'父顶点':>8}   本轮松弛次数")
    for e in res["trace"]:
        print(f"{e[0]:<6}{e[1]:<6}{e[2]:>10.2f}{e[3]:>8}   {e[4]}")
    if res["settled"] > len(res["trace"]):
        print(f"...（共确定 {res['settled']} 个顶点，此处仅显示前 {len(res['trace'])} 个）")

    print("-" * 78)
    amo = make_adj_map(edges)
    print(f"{'顶点':<6}{'最短距离':>10}   路径")
    for v in range(n):
        if res["dist"][v] == INF:
            print(f"{v:<6}{'inf':>10}   （不可达）")
        else:
            p = build_path(res["prev"], source, v)
            print(f"{v:<6}{res['dist'][v]:>10.2f}   " + " -> ".join(map(str, p)))

    ok, msg = verify(n, edges, source, res, amo)
    print("-" * 78)
    print(f"入队结点 {res['pushed']}，确定顶点 {res['settled']}，"
          f"松弛 {res['relax']} 次，剪枝 {res['pruned']} 次")
    print(f"结果校验  : {'通过' if ok else '失败'}（{msg}）")
    return res


def verify(n, edges, source, res, adj_map=None):
    """校验：① 每个可达顶点的路径确实是图中的一条合法路径；
    ② 路径权和与 dist 一致；③ 与 Bellman-Ford 结果相同。"""
    adj_map = adj_map or make_adj_map(edges)
    for v in range(n):
        if res["dist"][v] == INF:
            continue
        p = build_path(res["prev"], source, v)
        if p is None or p[0] != source or p[-1] != v:
            return False, f"顶点 {v} 的路径不连通"
        for a, b in zip(p, p[1:]):
            if (a, b) not in adj_map:
                return False, f"路径 {p} 中存在不存在的边 ({a},{b})"
        if abs(path_length(p, adj_map) - res["dist"][v]) > EPS:
            return False, f"顶点 {v} 的路径长度与 dist 不一致"
    ref = bellman_ford(n, edges, source)
    for v in range(n):
        a, b = res["dist"][v], ref[v]
        if (a == INF) != (b == INF) or (a != INF and abs(a - b) > EPS):
            return False, f"顶点 {v}: BB={a} 与 Bellman-Ford={b} 不一致"
    return True, "ok"


def run_demo():
    print("单源最短路径问题 · 分支限界法（优先队列式）交互式演示")

    # 演示 1：教材经典有向图（5 个顶点）
    n1 = 5
    e1 = [(0, 1, 10), (0, 4, 5), (1, 2, 1), (1, 4, 2), (2, 3, 4),
          (3, 0, 7), (3, 2, 6), (4, 1, 3), (4, 2, 9), (4, 3, 2)]
    _print_case("【演示 1】教材经典算例：|V| = 5，源点 s = 0", n1, e1, 0)

    # 演示 2：含不可达顶点与重边的图
    n2 = 6
    e2 = [(0, 1, 7), (0, 2, 9), (0, 5, 14), (1, 2, 10), (1, 3, 15),
          (2, 3, 11), (2, 5, 2), (3, 4, 6), (5, 4, 9), (0, 1, 4)]
    _print_case("【演示 2】含重边（0->1 有 7 和 4 两条）与多跳绕行的图",
                n2, e2, 0)

    # 演示 3：随机稀疏图，与 Floyd-Warshall 全源结果对照
    print("=" * 78)
    print("【演示 3】随机稀疏图（|V| = 30，|E| = 120），与 Floyd-Warshall 对照")
    print("-" * 78)
    random.seed(20240521)
    n3 = 30
    e3 = []
    for i in range(n3):
        for _ in range(4):
            j = random.randrange(n3)
            if j != i:
                e3.append((i, j, random.randint(1, 100)))
    t0 = time.perf_counter()
    res3 = shortest_path_bb(n3, e3, 0)
    t_bb = (time.perf_counter() - t0) * 1000
    t0 = time.perf_counter()
    D = floyd(n3, e3)
    t_fl = (time.perf_counter() - t0) * 1000
    same = all((res3["dist"][v] == INF and D[0][v] == INF) or
               (res3["dist"][v] != INF and D[0][v] != INF and
                abs(res3["dist"][v] - D[0][v]) < EPS) for v in range(n3))
    print(f"分支限界法      : {t_bb:.3f} ms，确定 {res3['settled']} 个顶点，"
          f"入队 {res3['pushed']} 个结点")
    print(f"Floyd-Warshall  : {t_fl:.3f} ms，O(n^3) = {n3 ** 3} 次运算")
    print(f"全源结果一致    : {'是' if same else '否'}")
    print(f"源点 0 到最远顶点距离: {max(d for d in res3['dist'] if d != INF):.2f}")

    # 交互输入
    print("=" * 78)
    if not sys.stdin.isatty():
        print("（非交互环境，跳过自定义图输入；如需交互请在终端中直接运行本程序）")
        return
    print("自定义图（直接回车使用默认值）：")
    try:
        n = int(_ask("  顶点数 |V| [默认 4]：", "4"))
        m = int(_ask("  边数 |E| [默认 5]：", "5"))
        s = int(_ask("  源点 s [默认 0]：", "0"))
    except ValueError:
        print("  输入不是整数，改用默认值 |V| = 4、|E| = 5、s = 0。")
        n, m, s = 4, 5, 0
    edges = []
    for i in range(m):
        try:
            u = int(_ask(f"  第 {i} 条边 起点 u [默认 0]：", "0"))
            v = int(_ask(f"  第 {i} 条边 终点 v [默认 1]：", "1"))
            w = int(_ask(f"  第 {i} 条边 权 w [默认 3]：", "3"))
        except ValueError:
            u, v, w = 0, 1, 3
        edges.append((u, v, w))
    try:
        _print_case("【自定义图】", n, edges, s)
    except ValueError as exc:
        print(f"错误：{exc}")


# --------------------------------------------------------------------------- #
# 模式二：自动功能对拍测试
# --------------------------------------------------------------------------- #
def run_check(verbose=True):
    print("单源最短路径问题 · 分支限界法自动对拍测试")
    print("-" * 78)
    passed = failed = 0
    failures = []

    def record(name, ok, msg=""):
        nonlocal passed, failed
        if ok:
            passed += 1
        else:
            failed += 1
            failures.append((name, msg))
            if verbose:
                print(f"[FAIL] {name}: {msg}")

    def case(name, n, edges, source, expect=None):
        res = shortest_path_bb(n, edges, source)
        ok, msg = verify(n, edges, source, res)
        if ok and expect is not None:
            for v, d in expect.items():
                if abs(res["dist"][v] - d) > EPS:
                    ok, msg = False, f"顶点 {v} 期望 {d}，实际 {res['dist'][v]}"
                    break
        record(name, ok, msg)
        return res

    # ---- 1. 固定与边界用例 ----
    print("[1/4] 固定与边界用例")
    case("单顶点无边的图", 1, [], 0, {0: 0})
    case("两点一条边", 2, [(0, 1, 5)], 0, {0: 0, 1: 5})
    case("存在不可达顶点", 3, [(0, 1, 3)], 0, {0: 0, 1: 3, 2: INF})
    case("重边取最小", 2, [(0, 1, 9), (0, 1, 4)], 0, {0: 0, 1: 4})
    case("自环不影响结果", 2, [(0, 0, 1), (0, 1, 2)], 0, {0: 0, 1: 2})
    case("链式图", 5, [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 4, 1)], 0,
         {0: 0, 1: 1, 2: 2, 3: 3, 4: 4})
    case("零权边", 3, [(0, 1, 0), (1, 2, 0)], 0, {0: 0, 1: 0, 2: 0})
    case("需要绕路的图", 4, [(0, 1, 10), (0, 2, 1), (2, 1, 1), (1, 3, 1)], 0,
         {0: 0, 1: 2, 2: 1, 3: 3})
    clrs_n = 5
    clrs_e = [(0, 1, 10), (0, 4, 5), (1, 2, 1), (1, 4, 2), (2, 3, 4),
              (3, 0, 7), (3, 2, 6), (4, 1, 3), (4, 2, 9), (4, 3, 2)]
    case("教材经典算例", clrs_n, clrs_e, 0, {0: 0, 1: 8, 2: 9, 3: 7, 4: 5})

    # ---- 2. 负权必须被拒绝 ----
    print("[2/4] 负权边检测（应显式报错而不是给出错误结果）")
    try:
        shortest_path_bb(3, [(0, 1, 2), (1, 2, -5)], 0)
        record("负权边报错", False, "未抛出异常")
    except ValueError:
        record("负权边报错", True)

    # ---- 3. 小规模随机图，全源与 Floyd-Warshall 对拍 ----
    print("[3/4] 小规模随机图对拍：所有源点 vs Floyd-Warshall（300 组）")
    random.seed(1)
    for t in range(300):
        n = random.randint(1, 8)
        m = random.randint(0, n * n)
        edges = []
        for _ in range(m):
            u = random.randrange(n)
            v = random.randrange(n)
            edges.append((u, v, random.randint(0, 20)))
        D = floyd(n, edges)
        ok_all, msg = True, ""
        for s in range(n):
            res = shortest_path_bb(n, edges, s)
            for v in range(n):
                a, b = res["dist"][v], D[s][v]
                if (a == INF) != (b == INF) or (a != INF and abs(a - b) > EPS):
                    ok_all, msg = False, f"case#{t} s={s} v={v}: BB={a}, Floyd={b}"
                    break
            if not ok_all:
                break
            ok2, m2 = verify(n, edges, s, res)
            if not ok2:
                ok_all, msg = False, f"case#{t} s={s}: {m2}"
                break
        record(f"random#{t}", ok_all, msg)

    # ---- 4. 中规模稀疏图，随机源点对拍 ----
    print("[4/4] 中规模稀疏图对拍：|V| <= 60、|E| ≈ 4|V|（200 组）")
    random.seed(2)
    for t in range(200):
        n = random.randint(5, 60)
        edges = []
        for u in range(n):
            for _ in range(4):
                v = random.randrange(n)
                if v != u:
                    edges.append((u, v, random.randint(1, 1000)))
        s = random.randrange(n)
        res = shortest_path_bb(n, edges, s)
        ref = bellman_ford(n, edges, s)
        ok_all, msg = True, ""
        for v in range(n):
            a, b = res["dist"][v], ref[v]
            if (a == INF) != (b == INF) or (a != INF and abs(a - b) > EPS):
                ok_all, msg = False, f"case#{t} v={v}: BB={a}, BF={b}"
                break
        if ok_all:
            ok_all, msg = verify(n, edges, s, res)
        record(f"sparse#{t}", ok_all, msg)

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
    """输出 CSV：scenario,n,edges,time_ms,settled,pushed,bf_time_ms。"""
    print("scenario,n,edges,time_ms,settled,pushed,bellman_ford_ms")
    random.seed(2024)

    def gen(n, per_vertex):
        edges = []
        for u in range(n):
            for _ in range(per_vertex):
                v = random.randrange(n)
                if v != u:
                    edges.append((u, v, random.randint(1, 1000)))
        return edges

    # 稀疏图：平均出度 4 ；稠密图：平均出度 20
    for scenario, sizes, per_vertex in (
        ("sparse", [200, 400, 800, 1200, 1600, 2000], 4),
        ("dense", [100, 200, 400, 600, 800, 1000], 20),
    ):
        for n in sizes:
            edges = gen(n, per_vertex)
            t0 = time.perf_counter()
            res = shortest_path_bb(n, edges, 0)
            t_bb = (time.perf_counter() - t0) * 1000.0

            if n <= 400:                      # Bellman-Ford 为 O(nm)，规模大时不再作基线
                t0 = time.perf_counter()
                bellman_ford(n, edges, 0)
                t_bf = (time.perf_counter() - t0) * 1000.0
                bf = f"{t_bf:.4f}"
            else:
                bf = ""

            print(f"{scenario},{n},{len(edges)},{t_bb:.4f},{res['settled']},"
                  f"{res['pushed']},{bf}")


# --------------------------------------------------------------------------- #
def main(argv=None):
    parser = argparse.ArgumentParser(
        description="单源最短路径问题（分支限界法）",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='运行方式：\n'
               '    python "02单源最短路径_分支限界法.py"            交互式功能演示\n'
               '    python "02单源最短路径_分支限界法.py" --check    自动功能对拍测试\n'
               '    python "02单源最短路径_分支限界法.py" --bench    性能测试（输出 CSV 数据）\n',
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
