from typing import List

# 2025.10.14 写的 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0 
        
        left = 0
        right = len(height) - 1
        while left < right:
            ans = max(ans, (right - left) * min(height[left], height[right]))
            # min()时间复杂度为O(1)，所以不会增加时间复杂度，总的时间复杂度还是O(n)。 
            # 所以这样写比我的写法更简洁一点。 
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return ans
    
#时间复杂度O(n) 
#空间复杂度O(1) 

# 2026.04.02 写的 
# 靠自己写出来的。 

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

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.02 11:15 