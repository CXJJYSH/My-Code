from cmath import inf
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1 
        
        m, n = len(nums1), len(nums2)

        left, right = 0, m 
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i 

            left1 = nums1[i - 1] if i > 0 else -inf 
            right1 = nums1[i] if i < m else inf 
            left2 = nums2[j - 1] if j > 0 else -inf 
            right2 = nums2[j] if j < n else inf 

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                
                return (max(left1, left2) + min(right1, right2)) / 2
            
            elif left1 > right2:
                right = i - 1
            
            else:
                left = i + 1

# B站波波微课的写法 

# 时间复杂度O(log min(m, n)) 
# 空间复杂度O(1) 

# 2026.05.18 12:46 

# 这里的二分搜索对象不是数组索引，而是分割线的位置（位置个数，从 0 前到 m - 1 后一共 m + 1 个）。 
# 之后再来进一步理解为什么二分要采取这种方式和边界条件。 

# 2026.05.18 12:51 