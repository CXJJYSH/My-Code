# ==============================
# 图的邻接矩阵表示（无向网）
# ==============================

class GraphAM:
    def __init__(self, vertex_num):
        self.vex_num = vertex_num
        # 初始化邻接矩阵，INF 表示不可达
        self.INF = float('inf')
        self.matrix = [[self.INF] * vertex_num for _ in range(vertex_num)]
        for i in range(vertex_num):
            self.matrix[i][i] = 0

    # 建立无向网的邻接矩阵
    def add_edge(self, u, v, w):
        self.matrix[u][v] = w
        self.matrix[v][u] = w

    # 返回顶点 u 在图中的位置
    def locate_vertex(self, u):
        return u

    # 返回与顶点 i 邻接的第一个顶点
    def first_adjacent(self, i):
        for j in range(self.vex_num):
            if self.matrix[i][j] != self.INF and i != j:
                return j
        return -1

    # 返回顶点 i 相对于顶点 j 的下一个邻接点
    def next_adjacent(self, i, j):
        for k in range(j + 1, self.vex_num):
            if self.matrix[i][k] != self.INF and i != k:
                return k
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
g = GraphAM(5)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 20)
g.add_edge(1, 3, 30)
g.add_edge(2, 4, 40)

print("BFS:", g.BFS(0))
print("DFS:", g.DFS(0))