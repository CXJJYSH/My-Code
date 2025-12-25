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