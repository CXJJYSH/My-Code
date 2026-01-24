class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        # 先处理边界条件。 
        # 有可以直接判断没有符合条件的答案的情况。 

        ans = 0
        prod = 1 # prod这里代表区间元素的乘积。 
        left = 0
        
        for right, x in enumerate(nums):
            prod *= x
            
            while prod >= k:
                prod /= nums[left]
                left += 1
            
            ans += right - left + 1
            # 循环外更新，这是更新符合条件的子数组个数。 

        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.24 23:37 