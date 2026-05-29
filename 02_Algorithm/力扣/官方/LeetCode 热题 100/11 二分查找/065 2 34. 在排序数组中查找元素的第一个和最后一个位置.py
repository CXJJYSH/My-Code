from typing import List

# 2025.10.31 

def lower_bound(nums, target):
    left = 0
    right = len(nums) - 1 # 闭。
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left 

def lower_bound2(nums, target):
    left = 0
    right = len(nums) # 左闭右开。
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left 

def lower_bound3(nums, target):
    left = -1
    right = len(nums) # 左开右开。
    while left < right - 1:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    return right # 或者left + 1

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = lower_bound3(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lower_bound3(nums, target + 1) - 1
        return [start, end]

    def lower_bound3(nums, target):
        left = -1
        right = len(nums) # 左开右开。
        while left < right - 1:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        return right # 或者left + 1

# 奥，就相当于力扣在测试代码是否正确时，是在我整段代码之后再进行代码中函数的调用的，所以所有的函数在它调用执行之前就已经被定义过。 

# 2026.05.16 12:03 

# 闭区间写法 

class Solution:
    def lower_bound(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
        
            if nums[mid] >= target:
                right = mid - 1
            else: 
                left = mid + 1
        
        return left 

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        start = self.lower_bound(nums, target)
        
        if start == len(nums) or nums[start] != target: # 前面是数组元素都小于target的情况，后面是数组元素都大于target的情况，前面left最终等于n，后面left最终等于0。 
            return [-1, -1]
        
        end = self.lower_bound(nums, target + 1) - 1
        
        return [start, end]
    
# 二分查找返回的是第一个等于或大于目标值的元素的下标。 
# 大于的情况可以举[1, 2, 4, 5]这个例子来理解。 

# 时间复杂度O(log n) 
# 空间复杂度O(1) 

# 2026.05.16 12:17 

# 2026.05.17 23:27 今天下午计组考试，考完去玩了，什么都没写。 