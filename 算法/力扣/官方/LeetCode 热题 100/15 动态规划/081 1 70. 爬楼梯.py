from functools import cache

# 递归 

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(i):
            if i <= 1:
                return 1 
            return dfs(i - 1) + dfs(i - 2)
        return dfs(n) 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 
    
# 循环 

class Solution:
    def climbStairs(self, n: int) -> int:
        f = [0] * (n + 1)
        f[0] = f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.05.26 12:05 

# 循环空间优化 

class Solution:
    def climbStairs(self, n: int) -> int:
        f0 = f1 = 1
        for _ in range(2, n + 1):
            new_f = f1 + f0
            f0 = f1 
            f1 = new_f 
        return f1 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.05.26 12:07 