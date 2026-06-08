# ==============================
# 图的邻接表表示（无向网）
# ==============================

class ArcNode:
    def __init__(self, adj_vex, weight):
        self.adj_vex = adj_vex
        self.weight = weight
        self.next = None


class VNode:
    def __init__(self, data):
        self.data = data
        self.first_arc = None


class GraphAL:
    def __init__(self, vertex_num):
        self.vex_num = vertex_num
        self.vertices = [VNode(i) for i in range(vertex_num)]

    # 建立无向网的邻接表
    def add_edge(self, u, v, w):
        arc1 = ArcNode(v, w)
        arc1.next = self.vertices[u].first_arc
        self.vertices[u].first_arc = arc1

        arc2 = ArcNode(u, w)
        arc2.next = self.vertices[v].first_arc
        self.vertices[v].first_arc = arc2

    # 返回顶点 u 在图中的位置
    def locate_vertex(self, u):
        return u

    # 返回与顶点 i 邻接的第一个顶点
    def first_adjacent(self, i):
        if self.vertices[i].first_arc:
            return self.vertices[i].first_arc.adj_vex
        return -1

    # 返回顶点 i 相对于顶点 j 的下一个邻接点
    def next_adjacent(self, i, j):
        p = self.vertices[i].first_arc
        while p:
            if p.adj_vex == j and p.next:
                return p.next.adj_vex
            p = p.next
        return -1

    # 广度优先遍历
    def BFS(self, start):
        visited = [False] * self.vex_num
        queue = [start]
        visited[start] = True
        result = []

        while queue:
            v = queue.pop(0)
            result.append(v)
            u = self.first_adjacent(v)
            while u != -1:
                if not visited[u]:
                    visited[u] = True
                    queue.append(u)
                u = self.next_adjacent(v, u)
        return result

    # 深度优先遍历
    def DFS(self, start):
        visited = [False] * self.vex_num
        result = []

        def dfs(v):
            visited[v] = True
            result.append(v)
            u = self.first_adjacent(v)
            while u != -1:
                if not visited[u]:
                    dfs(u)
                u = self.next_adjacent(v, u)

        dfs(start)
        return result


# 示例
g = GraphAL(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 20)
g.add_edge(1, 3, 30)
g.add_edge(2, 4, 40)

print("BFS:", g.BFS(0))
print("DFS:", g.DFS(0))