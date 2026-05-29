from typing import List

# 方法一：从答案的角度————倒序枚举。

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i):
            d = k - len(path)
            
            if i < d:
                return
            # 注定无法构成答案时剪枝。

            if len(path) == k: # 也可以直接d == 0，我感觉d == 0更直观易懂。
                ans.append(path.copy())
                return 
            # 边界条件。

            for j in range(i, 0, -1):
                path.append(j)
                dfs(j - 1)
                path.pop()
            # 非边界条件，“修改——回复”。

        dfs(n)

        return ans 

# 以下是方法一的优化版，将if i < d: return优化到循环for j in range(i, d - 1, -1)里，i >= n 时能正常进入循环，i < n 时不进入循环。
    
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i):
            d = k - len(path)
            if len(path) == k:
                ans.append(path.copy())
                return 
            for j in range(i, d - 1, -1):
                path.append(j)
                dfs(j - 1)
                path.pop()
        dfs(n)
        return ans 
    
# 时间复杂度O(k * C(n, k))
# 空间复杂度O(k)

# 中等
    
# 2025.12.02 15:34 

# 方法二：从输入的角度————选或不选，从末尾开始倒着选。

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        
        def dfs(i):
            d = k - len(path)

            if d == 0:
                ans.append(path.copy())
                return 
            
            # 不选i。
            # if语句是为了保证还有足够的可以构成答案的元素。
            if i > d:
                dfs(i - 1)

            # 选i。
            # 直接“修改——回复”。
            path.append(i)
            dfs(i - 1)
            path.pop()
        
        dfs(n)

        return ans 
    
# 时间复杂度O(k * C(n, k))
# 空间复杂度O(k)

# 中等
    
# 2025.12.02 15:47 