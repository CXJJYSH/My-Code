from bisect import bisect_left
from functools import cache
from typing import List

# 记忆化搜索写法 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache 
        
        def dfs(i):
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1
        
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        
        return ans 
    
# 记忆化搜索简洁写法 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        @cache 
        
        def dfs(i):
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1
        
        return max(dfs(i) for i in range(n)) 
        # 将最后四行改成一行。 

# 时间复杂度O(n ^ 2)， 
# 因为最后return的循环有O(n)的时间复杂度，每个状态里又有O(n)的循环， 
# 而递归下去的状态因为记忆化搜索不会产生新的时间复杂度，所以综合来看是O(n ^ 2)。 

# 空间复杂度O(n)， 
# 考虑记忆化搜索用的O(n)空间复杂度和第一次如果产生完整递归链的空间复杂度O(n)相加。 

# 分析链接：https://chatgpt.com/c/693f9739-2adc-8321-9a5f-ccc446d52c85（要用海外节点打开）。 

# 递推 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        f = [0] * n 
        
        for i in range(n):
            
            for j in range(i):
                if nums[j] < nums[i]:
                    f[i] = max(f[i], f[j])
            
            f[i] += 1 # 这里是要等所有和i有关的前置情况都计算完之后才能保证此时的f[i]最大，然后才能放心地加一。 
        
        return max(f) # 最后返回数组中的最大值即可。 
    
# 时间复杂度O(n ^ 2) 
# 空间复杂度O(n) 

# 递推 的时间复杂度和空间复杂度比 记忆化搜索 的更直观、更好理解。但是记忆化搜索的理解了一次之后，之后的也就没什么难度了。 

# 2025.12.15 13:33 

# 贪心 + 二分 写法 
# TMD太屌了 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        g = []
        
        for x in nums:
            j = bisect_left(g, x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x 
        
        return len(g)
    
# 看起来这段代码也太简洁了，但是简洁的代码背后的逻辑很难想到。 
# 竟然交换了动态规划的状态和状态值，原来是末尾元素对应的长度，现在竟然变成了长度对应的末尾元素，具体逻辑还得看灵神视频。 

# 时间复杂度O(n * log n)，循环O(n)乘上二分查找O(log n) 
# 空间复杂度O(n)，g的长度。 

# 2025.12.15 15:59 

# 下面的方法还把空间复杂度优化成O(1)了，更吓人。 

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ng = 0 # 表示看作的g数组的长度。 
        
        for x in nums:
            j = bisect_left(nums, x, 0, ng) # 把nums的一部分看成g数组，在[0, ng)范围内查找，j会等于ng。 
            if j == ng: # 添加到末尾 
                nums[j] = x # 这里写成nums[ng] = x也是一样有效的。 
                ng +=1 
            else: # 添加到中间 
                nums[j] = x 
        
        return ng # 返回看作的长度。 
    
# 时间复杂度O(n * log n) 
# 空间复杂度O(1) 

# 2025.12.15 16:07 

# 如果改成可以有相同元素的话，将bisect_left改成bisect_right即可。 

# 2025.12.15 16:11 