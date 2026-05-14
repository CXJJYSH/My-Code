from typing import List

# 2025.12.03 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2 * n
        ans = []
        path = []
        def dfs(i, balance):
            if len(path) == n:
                s = [")"] * m 
                for j in path:
                    s[j] = "("
                ans.append("".join(s))
                return 
            for right in range(balance + 1):
                path.append(i + right)
                dfs(i + right + 1, balance - right + 1)
                path.pop()
        dfs(0, 0)
        return ans 
    
# 2026.05.14 14:31 

# 选或不选 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = [''] * (n * 2)

        def dfs(left, right):
            if right == n:
                ans.append(''.join(path))
                return 
            
            if left < n:
                path[left + right] = '('
                dfs(left + 1, right)
            
            if right < left:
                path[left + right] = ')'
                dfs(left, right + 1)
        
        dfs(0, 0)
        return ans 
    
# 何时要恢复现场，何时不要恢复现场？

# path是空列表时要恢复现场，因为不能回头直接修改， 不恢复会产生位置错误。 
# path是固定长度的列表时不用恢复现场，因为可以直接用索引进行多次修改。 
    
# 每个条件判断只是确定当前状态然后向下递归而已，下一条判断又会确定新的当前状态然后向下递归，所以结果是正确的。 

# 时间复杂度O(n * C(2n, n))，公式为 路径长度 * 搜索树的叶子树（不同情况数 * 每种情况的深度）。 
# 空间复杂度O(n)，返回值的空间不计。 

# 2026.05.14 14:44 

# 枚举选哪个 

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        path = []

        def dfs(i, balance):
            if len(path) == n:
                s = [')'] * (n * 2)
                for j in path:
                    s[j] = '('
                ans.append(''.join(s))
                return 
            
            for right in range(balance + 1):
                path.append(i + right)
                dfs(i + right + 1, balance - right + 1)
                path.pop()

        dfs(0, 0)
        return ans 
    
# 时间复杂度O(n * C(2n, n)) 
# 空间复杂度O(n) 

# 2026.05.14 15:02 