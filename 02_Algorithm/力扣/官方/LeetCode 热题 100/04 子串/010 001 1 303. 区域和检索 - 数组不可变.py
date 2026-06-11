from typing import List

# 2025.11.10 
# 2026.02.03 

class NumArray:

    def __init__(self, nums: List[int]):
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x 
        self.s = s 

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left] 

# 2026.06.11 16:33 

class NumArray:

    def __init__(self, nums: List[int]):
        s = [0] * (len(nums) + 1) 
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x 
        self.s = s

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right + 1] - self.s[left] 

# 2026.06.11 16:40 