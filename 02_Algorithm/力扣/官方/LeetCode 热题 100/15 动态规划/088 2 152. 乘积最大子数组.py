from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums) 

        f_max = [0] * n 
        f_min = [0] * n 

        f_max[0] = f_min[0] = nums[0]

        for i in range(1, n):
            x = nums[i] 

            f_max[i] = max(f_max[i - 1] * x, f_min[i - 1] * x, x) 
            f_min[i] = min(f_max[i - 1] * x, f_min[i - 1] * x, x)

        return max(f_max) 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 226.05.28 16:36 

# 优化写法没写，之后有机会再来写。 
# https://leetcode.cn/problems/maximum-product-subarray/?envType=study-plan-v2&envId=top-100-liked 

# 2026.05.28 16:37 