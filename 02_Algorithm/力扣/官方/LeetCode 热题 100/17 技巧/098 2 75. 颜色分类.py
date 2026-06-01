from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        p0 = p1 = 0 
        
        for i, x in enumerate(nums):
            nums[i] = 2 # 如果是2的话只要进行这一步，之后的都进行不了。 
        
            if x <= 1: # 如果是1的话进行到这一步，下一步进行不了了。 
                nums[p1] = 1
                p1 += 1
        
            if x == 0: # 如果是0的话要经历上面的三步。 
                nums[p0] = 0
                p0 += 1

# 实际上就是对题目给的数组进行插入排序，每次遍历到下一个元素，将该元素插入到前面元素组成的有序数组中，执行逻辑和上面代码一致。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.06.01 18:58 