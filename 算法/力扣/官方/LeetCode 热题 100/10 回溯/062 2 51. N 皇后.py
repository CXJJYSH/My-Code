from typing import List

# 2025.12.05 

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = [] 
        col = [0] * n 
        on_path = [False] * n 
        m = 2 * n + 1
        diag1 = [False] * m 
        diag2 = [False] * m 
        def dfs(r):
            if r == n:
                ans.append(["." * c + "Q" + "." * (n - 1 - c) for c in col])
                return 
            for c in range(n):
                if not on_path[c] and not diag1[r + c] and not diag2[r - c]:
                    col[r] = c 
                    on_path[c] = diag1[r + c] = diag2[r - c] = True 
                    dfs(r + 1)
                    on_path[c] = diag1[r + c] = diag2[r - c] = False 
        dfs(0)
        return ans 
    
# 2026.05.15 

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        
        queens = [0] * n # 这是用行号r作索引，记录该行皇后位于哪一列的列表（数组） 
        
        col = [False] * n # 这是记录某一列有没有放皇后的列表（数组） 

        diag1 = [False] * (n * 2 - 1) # 乘上一个方向不同结果的斜线个数 
        diag2 = [False] * (n * 2 - 1) # 乘上一个方向不同结果的斜线个数 
        # 这两个是记录两条斜线上有没有冲突的皇后的列表（数组） 

        def dfs(r):
            if r == n:
                ans.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in queens]) # 这是遵守题目要求的返回格式 
                return 

            for c, ok in enumerate(col):
                if not ok and not diag1[r + c] and not diag2[r - c]: # 没皇后就可以先放着试试，之后恢复现场。 
                    queens[r] = c 

                    col[c] = diag1[r + c] = diag2[r - c] = True 
                    dfs(r + 1)
                    col[c] = diag1[r + c] = diag2[r - c] = False 

        dfs(0) # 从第一行开始递归。 

        return ans 
    
# 这是一个很基础但非常关键的复杂度分析逻辑：在计算机科学中，如果你需要“触摸”或者“写满”一个多大的空间，你就必须付出同等规模的时间。 
# 时间复杂度O(n! * (n ** 2))，至多 n! 中情况，每个情况创建 n × n 的网格要花费 O(n ** 2) 时间复杂度，总体时间复杂度为 O(n! * (n ** 2)) 。 
# 空间复杂度O(n)，r决定递归深度O(n)，queens、col、diag1、diag2都是O(n)，返回值不计，总体空间复杂度O(n)。 

# 2026.05.15 12:28 