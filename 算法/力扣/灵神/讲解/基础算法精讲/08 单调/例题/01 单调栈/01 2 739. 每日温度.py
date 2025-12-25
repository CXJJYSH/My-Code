from typing import List

# 从右到左 写法 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n 
        st = [] # 建立一个栈。 
        
        for i in range(n - 1, -1, -1):
            t = temperatures[i] 
            
            while st and t >= temperatures[st[-1]]:
                st.pop()
                # Python中用列表数据结构表示栈时，列表的最后一个元素才表示栈顶元素，引用时下标要用-1表示。 

            if st:
                ans[i] = st[-1] - i 
            
            st.append(i)
            # 栈里面保存的是温度对应的索引。 

        return ans 
    
# 2025.12.25 23:59 
    
# 因为每个元素最多入栈一次、最多出栈一次，总操作数最多为2 * n，所以 
# 时间复杂度O(n) 

# 因为最坏情况下，所有温度元素都相等，栈需要存储全部元素，占用O(n)空间，所以从这角度来说 
# 空间复杂度O(n) 
# 但是这道题值域很小，30 <= t <= 100，栈最多存储71个元素，所以在值域很小的情况下，总数据量用U表示，那么 
# 空间复杂度O(min(n, U))，U = max - min + 1 

# 2025.12.26 00:16 