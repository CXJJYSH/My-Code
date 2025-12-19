from cmath import inf
from functools import cache
from typing import List

# 记忆化搜索写法 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        @cache
        
        def dfs(i, hold):
            if i < 0:
                return -inf if hold else 0 
            if hold:
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
            # 因为这里是return，要执行必执行其一，所以不需要采用if - else结构。 
            
        return dfs(n - 1, False) 
    
# 时间复杂度O(n)，一共O(n)个状态，每个状态的计算时间是O(1)，所以总时间复杂度是O(n)。 
# 空间复杂度O(n)，一共有O(n)个状态，所以空间复杂度是O(n)。 

# 2025.12.16 19:42 

# 递推写法 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        f = [[0] * 2 for _ in range(n + 1)]
        f[0][1] = -inf
        # 领悟： 
        # 递归写法的参数对应着递推写法数组的维度，这里是前面的i对应着数组的第一个维度，后面的hold对应着数组的第二个维度。 
        # 参数的取值范围对应着维度的范围，i的取值范围为0到n，所以第一个维度的取值范围为0到n， 
        # 而hold只有两种取值，对应的第二个维度长度大小也为2，对应的索引为0和1，所以可以在第二个维度用0和1的下标表示未持有和持有两种状态， 
        # 而不需要针对两种状态分别初始化两次。 
        
        for i, p in enumerate(prices):
            f[i + 1][0] = max(f[i][0], f[i][1] + p)
            f[i + 1][1] = max(f[i][1], f[i][0] - p)
        
        return f[n][0] 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2025.12.16 19:58 

# 递推写法空间优化 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f0 = 0
        f1 = -inf 
        
        for p in prices:
            new_f0 = max(f0, f1 + p)
            f1 = max(f1, f0 - p)
            f0 = new_f0 
        
        return f0 
    
# 太牛逼了吧，只要找对了状态定义和状态转移方程，并确定了边界条件、初始化好了边界条件，就能将代码写得如此简洁， 
# 这就是动态规划吗，太牛逼了，恐怖如斯。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2025.12.16 20:05 