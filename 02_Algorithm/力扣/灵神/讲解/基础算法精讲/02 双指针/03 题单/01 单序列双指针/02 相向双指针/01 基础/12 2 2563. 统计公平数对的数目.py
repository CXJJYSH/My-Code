from bisect import bisect_left, bisect_right
from typing import List

# 二分查找方法 

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        ans = 0

        for j, x in enumerate(nums):
            r = bisect_right(nums, upper - x, 0, j)
            l = bisect_left(nums, lower - x, 0, j)

            ans += r - l

        return ans 
    
# 时间复杂度O(n log n)，nums.sort()的。 
# 空间复杂度O(1) 

# 2026.03.20 12:36 

# 二分查找的内置函数用法 
# 找所有小于上边界的就用right将指针放在所有小的数的右边，这样指针大小刚好是小的数个数。 
# 找所有小于下边界的就用left将指针放在所有大的数的左边，这样指针大小刚好是小的数的个数。 

# 2026.03.20 12:43 

# 三指针写法 

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        
        ans = 0
        
        n = len(nums) 
        left = n
        right = n 
        
        for j, x in enumerate(nums):
            while right and nums[right - 1] > upper - x: # 要进入刚好小于等于上边界的区间。 
                # right从n开始，索引从right - 1，即n - 1开始。 
                # while right使right在1结束，索引在0结束。 
                right -= 1
            while left and nums[left - 1] >= lower - x: # 要进入刚好小于下边界的区间。 
                # left从n开始，索引从left - 1，即n - 1开始。 
                # while left使left在1结束，索引在0结束。 
                left -= 1
        
            ans += min(right, j) - min(left, j)
            # 每次统计都是从当前的数对右侧往前找数对左侧，所以为了不重复记和漏记，应该只在j左侧统计数对左侧，所以要取最小值。 
        
        return ans 
    
# 时间复杂度O(n log n)，nums.sort()。 
# 空间复杂度O(1) 

# 2026.03.20 14:12 

# 2026.03.20 14:24 

# 相向双指针写法 

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        
        def count(upper: int) -> int:
            res = 0
        
            j = len(nums) - 1
            for i, x in enumerate(nums):
                while j > i and nums[j] > upper - x:
                    j -= 1
        
                if j == i:
                    break
        
                res += j - i 
        
            return res 
        
        return count(upper) - count(lower - 1) 
    
# 这里的双指针是一个动一下之后另一个动一轮。 
# 将找小于某个数的所有元素的代码写成了一个函数。 
# 先找小于等于上边界的，再找小于下边界的，小于下边界的要转化为小于等于下边界减一的。 

# 时间复杂度O(n log n) 
# 空间复杂度O(1) 

# 2026.03.20 15:49 

# 这三种方法时间速度越来越快，第一种74.59%，第二种83.91%，第三种89.63%。 

# 2026.03.20 15:54 