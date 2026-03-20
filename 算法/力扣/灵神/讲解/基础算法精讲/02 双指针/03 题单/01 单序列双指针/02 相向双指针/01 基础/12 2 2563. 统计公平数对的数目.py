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