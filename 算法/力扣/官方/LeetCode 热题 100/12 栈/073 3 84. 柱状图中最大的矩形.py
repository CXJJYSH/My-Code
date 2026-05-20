from typing import List

# 最基础的三次遍历 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        left = [-1] * n 
        st = []
        for i, h in enumerate(heights):
            while st and heights[st[-1]] >= h:
                st.pop()
            if st: # 剩下的只有小于h的。 
                left[i] = st[-1] # 取出小于h的最近索引。 
            st.append(i)

        right = [n] * n 
        st.clear()
        for i in range(n - 1, -1, -1):
            h = heights[i]
            while st and heights[st[-1]] >= h:
                st.pop()
            if st:
                right[i] = st[-1] # 和上面一样取出小于h的最近索引。 
            st.append(i)
        
        ans = 0
        for h, l, r in zip(heights, left, right):
            ans = max(ans, h * (r - l - 1))

        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.05.20 22:13 

# 两次遍历 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        left = [-1] * n 
        right = [n] * n 
        st = []
        
        for i, h in enumerate(heights):
            while st and heights[st[-1]] >= h:
                right[st.pop()] = i 
            if st:
                left[i] = st[-1]
            st.append(i)

        ans = 0
        for h, l, r in zip(heights, left, right):
            ans = max(ans, h * (r - l - 1))

        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.05.20 22:25 

# 一次遍历，这里是直接枚举right了，和之前枚举最高高度不一样了。 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        st = [-1]

        ans = 0
        for right, h in enumerate(heights):
            while len(st) > 1 and heights[st[-1]] >= h:
                i = st.pop()
        
                left = st[-1]
        
                ans = max(ans, heights[i] * (right - left - 1))
        
            st.append(right)
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(min(n, U))，U为heights中不同元素个数，栈中没有重复元素。 

# 2026.05.20 22:32 