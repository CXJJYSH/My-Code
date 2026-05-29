from functools import cache
from typing import List

# 递归 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache 

        def dfs(i, j):
            if i < 0:
                return j == 0
            
            if j < nums[i]:
                return dfs(i - 1, j)
            
            return dfs(i - 1, j - nums[i]) or dfs(i - 1, j) 
        
        s = sum(nums) 
        
        return s % 2 == 0 and dfs(len(nums) - 1, s // 2) 
    
# 时间复杂度O(n * s) 
# 空间复杂度O(n * s) 

# 2026.05.28 16:46 

# 递归逻辑优化 

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache 

        def dfs(i: int, j: int) -> bool:
            if i < 0:
                return j == 0
            return (j >= nums[i] and dfs(i - 1, j - nums[i])) or dfs(i - 1, j)
            # and优先级大于or 

        s = sum(nums)

        return s % 2 == 0 and dfs(len(nums) - 1, s // 2)
    
# 循环之后有机会再写 
# https://leetcode.cn/problems/partition-equal-subset-sum/solutions/2785266/0-1-bei-bao-cong-ji-yi-hua-sou-suo-dao-d-ev76/?envType=study-plan-v2&envId=top-100-liked 

# 2026.05.28 16:52 