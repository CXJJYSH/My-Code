from typing import List

# 2025.12.25 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        st = []
        for i, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:
                j = st.pop() 
                ans[j] = i - j
            st.append(i)
        return ans 

# 2026.05.20 12:57 

# 从右到左 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures) 
        ans = [0] * n 
        st = []

        for i in range(n - 1, -1, -1):
            t = temperatures[i]
        
            while st and t >= temperatures[st[-1]]:
                st.pop() 
            # 把栈中小于当前温度的元素全部弹出来。 
        
            if st:
                ans[i] = st[-1] - i # 这里算的是几天后。 
        
            st.append(i) # 存温度的索引 
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(min(n, U)，U = max(temperatures) - min(temperatures) + 1。 

# 2026.05.20 13:00 

# 2026.05.20 21:14 

# 从左到右 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n 
        st = []
        
        
        for i, t in enumerate(temperatures):
            while st and t > temperatures[st[-1]]:
                j = st.pop()
                ans[j] = i - j
        
            st.append(i) 
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n)，这种写法栈中可以有重复元素。 

# 2026.05.20 21:15 