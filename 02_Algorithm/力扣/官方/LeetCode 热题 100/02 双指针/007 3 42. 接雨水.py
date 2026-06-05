from typing import List

# 2025.10.14 
# 2025.12.27 
# 2026.04.03 

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        pre_max = 0
        suf_max = 0
        left = 0
        right = len(height) - 1
        while left < right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else: 
                ans += suf_max - height[right]
                right -= 1
        return ans 
    
# 2026.06.05 11:02 

# 前后缀分解（没看） 

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        pre_max = [0] * n  # pre_max[i] 表示从 height[0] 到 height[i] 的最大值
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        suf_max = [0] * n  # suf_max[i] 表示从 height[i] 到 height[n-1] 的最大值
        suf_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        ans = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            ans += min(pre, suf) - h  # 累加每个水桶能接多少水
        return ans

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.06.05 11:03 

# 相向双指针 

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0

        pre_max = suf_max = 0 
        
        left, right = 0, len(height) - 1
        
        while left < right:
            pre_max = max(pre_max, height[left]) 
            suf_max = max(suf_max, height[right]) 

            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right] 
                right -= 1 
            
        return ans 
    
# 每次写这个接雨水题目都有新的收获。 

# 现在更加觉得这个相向双指针的方法很好理解了，牛逼，下次争取自己写出来。 
# 维护最高的水池边，每一段单独计算水柱高度。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.06.05 11:10 