from typing import List

# 2025.10.14 
# 2026.04.02 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] <= height[right]:
                res = (right - left) * height[left]
                ans = max(ans, res)
                left += 1
            else: 
                res = (right - left) * height[right]
                ans = max(ans, res)
                right -= 1
        return ans 
    
# 2026.06.05 10:44 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0 

        left = 0
        right = len(height) - 1
        
        while left < right:
            area = (right - left) * min(height[left], height[right]) 
            ans = max(ans, area) 
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.06.05 10:48 