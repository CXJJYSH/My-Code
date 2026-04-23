from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(i: int, j: int) -> None: # 定义一个反转函数。 
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        
        n = len(nums)
        k %= n

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

# 最后运用两次反转抵消反转的性质。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.16 12:51 