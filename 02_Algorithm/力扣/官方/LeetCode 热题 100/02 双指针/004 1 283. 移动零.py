from typing import List

# 2025.10.09 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        stack_size = 0
        for x in nums:
            if x:
                nums[stack_size] = x
                stack_size += 1
        for i in range(stack_size, len(nums)):
            nums[i] = 0
        '''
        '''
        stack_size = 0
        for x in nums:
            if x:
                nums[stack_size] = x
                stack_size += 1
        nums[stack_size:] = [0] * (len(nums) - stack_size)
        '''
        
        i0 = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[i0] = nums[i0], nums[i]
                i0 += 1 

# 2026.06.05 10:36 

# 原地栈（把nums当作栈）。 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        stack_size = 0 

        for x in nums:
            if x: 
                nums[stack_size] = x 
                stack_size += 1
        
        for i in range(stack_size, len(nums)):
            nums[i] = 0 

# 双指针 

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i0 = 0 

        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[i0] = nums[i0], nums[i]
                i0 += 1

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.06.05 10:43 