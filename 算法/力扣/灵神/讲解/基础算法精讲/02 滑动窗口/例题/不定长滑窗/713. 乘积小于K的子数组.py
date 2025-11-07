class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        
        # 这是从不满足题目条件到满足题目条件的题。
        
        # 看了灵神的视频，一遍就过了，比较简单。
        # 灵神提示说“右端点是固定的，找右端点左边符合要求的子数组个数”是重点，要记住。
        
        if k <= 1:
            return 0
        ans = 0
        prod = 1
        left = 0
        for right, x in enumerate(nums):
            prod *= x
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans