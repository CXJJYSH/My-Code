from bisect import bisect_left
from functools import cache
from typing import List

# 2025.12.15 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ng = 0
        for x in nums:
            j = bisect_left(nums, x, 0, ng)
            if j == ng:
                nums[ng] = x 
                ng +=1 
            else:
                nums[j] = x 
        return ng 
    
# 2026.05.28 14:25 

# 递归 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache

        def dfs(i):
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j)) 
            return res + 1

        return max(dfs(i) for i in range(len(nums))) 
    
# 时间复杂度O(n ** 2)，状态数O(n)，单个状态计算时间为O(n)。 
# 空间复杂度O(n) 

# 2026.05.28 14:32 

# 循环 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        f = [0] * len(nums) 

        for i, x in enumerate(nums):
        
            for j, y in enumerate(nums[:i]):
                if y < x:
                    f[i] = max(f[i], f[j])
            f[i] += 1
        
        return max(f) 
    
# 时间复杂度O(n ** 2) 
# 空间复杂度O(n) 

# 2026.05.28 14:34 

# 还有贪心 + 二分查找的做法，但是现在我就先不管了，之后再回来做。 
# https://leetcode.cn/problems/longest-increasing-subsequence/solutions/2147040/jiao-ni-yi-bu-bu-si-kao-dpfu-o1-kong-jia-4zma/?envType=study-plan-v2&envId=top-100-liked 

# 2026.05.28 14:35 