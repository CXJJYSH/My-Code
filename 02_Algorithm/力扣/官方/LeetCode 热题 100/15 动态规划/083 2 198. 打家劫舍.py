from functools import cache
from typing import List

# 2025.12.08 

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        f0 = f1 = 0 
        for i, x in enumerate(nums):
            new_f = max(f1, f0 + x) 
            f0 = f1 
            f1 = new_f 
        return f1 
    
# 2026.05.26 12:21 

# 递归 

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache

        def dfs(i):
            if i < 0:
                return 0
        
            return max(dfs(i - 1), dfs(i - 2) + nums[i]) # 其实这里就是选与不选。 
        
        return dfs(len(nums) - 1) 
    
# 时间复杂度O(n) 
# 空间复杂度O(n)，递归要O(n)空间。  

# 2026.05.26 12:22 

# 循环 

class Solution:
    def rob(self, nums: List[int]) -> int:
        f = [0] * len(nums + 2)

        for i, x in enumerate(nums):
            f[i + 2] = max(f[i + 1], f[i] + x)
        
        return f[-1]

# 现在不太清楚下标越界是发生的什么地方，之前可能清楚。 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.05.26 12:26 

class Solution:
    def rob(self, nums: List[int]) -> int:
        f0 = f1 = 0

        for x in nums:
            f0, f1 = f1, max(f1, f0 + x)

        return f1 
    
# OK，完全会写了。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.05.26 12:27 