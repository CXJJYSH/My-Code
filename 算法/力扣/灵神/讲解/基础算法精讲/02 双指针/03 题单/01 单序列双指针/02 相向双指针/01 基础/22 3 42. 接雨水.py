from typing import List

# 2025.10.14 
# 2025.12.27 写的代码 

class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        #时间复杂度O(n)
        #空间复杂度O(n)
        n = len(height)
        pre_max = [0] * n
        pre_max[0] = height[0]
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])
        suf_max = [0] * n
        suf_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])
        ans = 0
        for h, pre, suf in zip(height, pre_max, suf_max):
            ans += min(pre, suf) - h 
        return ans 
        
        #优化
        #时间复杂度O(n)
        #空间复杂度O(1)
        n = len(height)
        ans = 0
        left = 0
        right = n - 1
        pre_max = 0
        suf_max = 0
        while left <= right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans 
        2025.12.27 00:10 之前的代码。 
        '''
        ans = 0
        st = []
        for i, h in enumerate(height):
            while st and h >= height[st[-1]]:
                bottom_h = height[st.pop()]
                if not st:
                    break
                left = height[st[-1]]
                dh = min(left, h) - bottom_h
                ans += dh * (i - st[-1] - 1)
            st.append(i)
        return ans 
    
# 2026.04.03 23:45 

# 相向双指针写法 

# 可以理解为左右两边最边上的柱子是当前水缸的两边， 
# 水缸能装的水由最短的柱子高度决定， 
# 计算方式为一格一格记每一格的水柱高度， 
# 遵循边界谁小谁移动的原则， 
# 左边小就左边界移动，相等或右边界小就右边界移动， 
# 更新边界使两边边界越来越大， 
# 逐步统计边界中各水柱的高度， 
# 每次统计时将高度计入答案， 
# 最后返回答案即可， 
# 这个方法从头开始模拟一遍算法就很好理解了。 

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        
        pre_max = 0
        suf_max = 0
        
        left = 0
        right = len(height) - 1
        while left < right:
            # 更新水缸边界。 
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
        
            # 谁小谁移动。 
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else: 
                ans += suf_max - height[right]
                right -= 1
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.03 23:46 
# 2026.04.03 23:51 