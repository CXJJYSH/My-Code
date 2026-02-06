from typing import List

# 这道题的难点在于原本的数组是无序的，而在无序情况下很难零散地计算要移除的元素究竟是多少。 
# 难点在于要想到首先将数组排序，然后用有序数组找无序情况下的最大值和最小值，用有序数组仍然可以找到正确的保留的元素的最多个数， 
# 之后只需要用总数减保留的元素的最多个数就可以了。 

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_save = 0
        left = 0
        
        for right, x in enumerate(nums):
            while x > nums[left] * k:
                left += 1
            
            max_save = max(max_save, right - left + 1)
        
        return len(nums) - max_save 
    
# 时间复杂度O(n log n)，因为nums.sort()排序时间复杂度比后面的循环大。 
# 空间复杂度O(1)，忽略排序的栈开销。 

# 2026.01.03 18:39 