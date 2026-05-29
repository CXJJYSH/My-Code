from typing import List

class NumArray:

    def __init__(self, nums: list[int]):
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x
        self.s = s 

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# 前缀和方法教学
# 2025.11.10 12:27 

# 2026.02.03 再来一遍 

class NumArray:

    def __init__(self, nums: List[int]):
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x 
        self.s = s 
        # 时间复杂度O(n) 

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left] 
        # 时间复杂度O(1) 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.02.03 16:30 