from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(len(nums)):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]: # 学号在范围内且对应的座位上的元素和学号不匹配。 
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i] # 交换两个位置上的元素，将正确的调前去，将未匹配的调后来。 
        
        for i in range(n):
            if nums[i] != i + 1: # if nums[0] != 0 + 1:
                return i + 1         # return 1 
        
        return n + 1 
    
# 时间复杂度O(n)，因为每次交换会调到一个正确位置，所以至多交换n次，时间复杂度为O(n)。 
# 空间复杂度O(1) 

# 2026.04.17 12:01 