from typing import List

# 2025.11.04 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = -1
        right = len(nums) - 1 # 这里赋len(nums)或len(nums) - 1都行。
        while left + 1 < right:
            mid = (left + right) // 2
            x = nums[mid]
            if target > nums[-1] >= x:
                right = mid
            elif x > nums[-1] >= target:
                left = mid
            elif x >= target:
                right = mid
            else:
                left = mid
        return right if nums[right] == target else -1
        '''
        def is_blue(i: int) -> bool:
            end = nums[-1]
            if nums[i] > end:
                return target > end and nums[i] >= target 
            else:
                return target > end or nums[i] >= target 
        left = -1
        right = len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid
            else:
                left = mid
        if right == len(nums) or nums[right] != target:
            return -1
        return right 
        '''
        '''
        def findMin(self, nums: List[int]) -> int:
            left = -1
            right = len(nums) - 1
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] < nums[-1]:
                    right = mid 
                else:
                    left = mid 
            return right

        def lower_bound(self, nums: List[int], left: int, right: int, target: int) -> int:
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid
            return right if nums[right] == target else -1

        def search(self, nums: List[int], target: int) -> int:
            i = self.findMin(nums)
            if target > nums[-1]:
                return self.lower_bound(nums, -1, i, target)
            return self.lower_bound(nums, i - 1, len(nums), target)
        '''

# 2026.05.18 11:40 

# 两次二分 

class Solution:
    def findMin(self, nums):
        left, right = -1, len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
        
            if nums[mid] < nums[-1]:
                right = mid 
            else:
                left = mid 
        
        return right 

    def lower_bound(self, nums, left, right, target):
        while left + 1 < right:
            mid = (left + right) // 2
        
            if nums[mid] >= target:
                right = mid 
            else:
                left = mid 
        
        return right if nums[right] == target else -1 

    def search(self, nums: List[int], target: int) -> int:
        i = self.findMin(nums)
        
        if target > nums[-1]:
            return self.lower_bound(nums, -1, i, target)
        
        return self.lower_bound(nums, i - 1, len(nums), target)
    
# 时间复杂度O(log n) 
# 空间复杂度O(1) 

# 2026.05.18 11:55 

# 一次二分 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = -1, len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2
        
            x = nums[mid]
        
            if target > nums[-1] >= x:
                right = mid 
            elif x > nums[-1] >= target:
                left = mid 
            elif x >= target:
                right = mid 
            else:
                left = mid 
        
        return right if nums[right] == target else -1 
        # 如果target不在nums里，nums[right] = target一定不成立，一定返回-1。 
    
# 时间复杂度O(log n) 
# 空间复杂度O(1) 

# 2026.05.18 12:00 

# 一次二分还有一种写法，但是懒得看了，之后有时间再来看。 

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def check(i: int) -> bool:
            x = nums[i]
            if x > nums[-1]:
                return target > nums[-1] and x >= target
            return target > nums[-1] or x >= target

        left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right if nums[right] == target else -1
    
# 2026.05.18 12:00 