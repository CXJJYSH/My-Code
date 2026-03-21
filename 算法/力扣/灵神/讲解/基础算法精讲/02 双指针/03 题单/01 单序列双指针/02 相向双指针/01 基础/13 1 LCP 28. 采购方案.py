from typing import List

class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = 0

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] <= target:
                ans += right - left 
                left += 1
            else:
                right -= 1

        return ans % 1000000007
    
# 最后由于题目说要对一个大数字取模，所以最后一局return的时候要写成 ans % 1000000007 。 

# 时间复杂度O(n log n)，nums.sort()。  
# 空间复杂度O(1) 

# 2026.03.21 23:22 