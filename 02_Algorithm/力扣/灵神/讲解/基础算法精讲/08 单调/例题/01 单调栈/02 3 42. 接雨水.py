from typing import List

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
        
        # 2025.12.27 00:10 之前的代码。 
        # 2025.10.14的代码。 

        '''
        ans = 0
        st = []

        for i, h in enumerate(height):
            while st and h >= height[st[-1]]: # 如果有底部柱子且找到了比底部柱子更高的柱子： 
                bottom_h = height[st.pop()]
                # 先用pop()方法拿到底部柱子的高度，同时底部柱子的索引也从栈顶弹出，露出左边柱子的索引，现在左边柱子的索引位于栈顶。 

                if not st: # if len(st) == 0: 
                    break
                # 这时候要检查合法性，如果弹出底部柱子之后没有可以作为左边柱子的柱子了，那么直接break跳出循环。 
                # 这个也可以说是在检查边界条件。 

                left = height[st[-1]] # 也可以left = st[-1]，前者是取高度，后者是取索引。 
                # 找左边柱子。 

                dh = min(left, h) - bottom_h # dh = min(height[left], h) - bottom_h 
                # 计算区域高度。 

                ans += dh * (i - st[-1] - 1) # ans = dh * (i - left - 1) 
                # 直接让答案加上 区域高度 × 区域宽度 进行更新。 
                # 宽度要减一，因为不包括两边的柱子。 
                # 如果包括两边的柱子，宽度就要加一。 
                # 如果只包含一个柱子，那就左右柱子的索引直接减，不需要加一或者减一。 

            st.append(i)
            # 循环外仍然要将当前元素的索引加入栈里。 

        return ans 
    
# 时空复杂度和 739. 每日温度 一样，都是 
# 时间复杂度O(n)，因为每个元素至多入栈一次并出栈一次，操作数为2 * n。 
# 空间复杂度O(n)，因为最坏情况下元素逐个减小，栈里要保存n个数据。 

# 2025.12.27 00:31 