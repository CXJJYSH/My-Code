from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a) 

        colors = [0] * numCourses 

        def dfs(x):
            colors[x] = 1
            for y in g[x]:
                if colors[y] == 1 or colors[y] == 0 and dfs(y):
                    return True 
            colors[x] = 2
            return False 

        for i, c in enumerate(colors):
            if c == 0 and dfs(i):
                return False # 代表不能全部修完。 
        return True # 代表能全部修完。 
    
# 时间复杂度O(n + m)，其中 n 是 numCourses，m 是 prerequisites 的长度。每个节点至多递归访问一次，每条边至多遍历一次。 
# 空间复杂度O(n + m)，存储 g 需要 O(n + m) 的空间。 

# 2026.05.12 11:37 