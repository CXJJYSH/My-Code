from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i, jump in enumerate(nums):
            if i > mx:
                return False 
            mx = max(mx, i + jump)
        return True 
    
# 小小剪枝一下 

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i, jump in enumerate(nums):
            if i > mx:
                return False 
            mx = max(mx, i + jump)
            if mx >= len(nums) - 1:
                return True 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 22026.05.25 11:44 