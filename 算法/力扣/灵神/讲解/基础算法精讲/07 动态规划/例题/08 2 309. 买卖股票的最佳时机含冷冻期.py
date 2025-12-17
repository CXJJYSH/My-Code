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
                return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i])
                # 语句含义分析：今天持有，分两种情况， 
                # 第一种是前一天持有，保持到今天， 
                # 第二种是前一天未持有，今天买入， 
                # 但是如果今天买入，因为题目规定了前一天不能卖出，所以昨天是继承的是前天操作结束之后未持有的状态。 
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
        
        return dfs(n - 1, False) 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2025.12.17 23:21 

# 递推写法 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        f = [[0] * 2 for _ in range(n + 2)]
        f[1][1] = -inf # 这里的边界条件有值得注意的地方：因为之前递归的边界条件是i = -1，这里整体数组加了2，那么边界条件就变成了i = 1。 
        
        for i, p in enumerate(prices):
            f[i + 2][0] = max(f[i + 1][0], f[i + 1][1] + p)
            f[i + 2][1] = max(f[i + 1][1], f[i][0] - p)
        
        return f[-1][0] 
        # 这里写成f[n + 1][0]效果也是一样的，因为这里-1和n + 1都表示的是数组最后一个元素，只不过-1是简便写法，n + 1是具体索引。 
        # 客观来说，用-1表示更简单，也更不容易出错，如果要用具体索引的话可能会算错。 

# 未空间优化 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2025.12.17 23:44 

# 递推写法空间优化 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre0 = 0
        f0 = 0
        f1 = -inf  
        # 之前的题目只有昨天的“持有”与“未持有”两种状态，只用使用个数为2的O(1)额外空间。 
        # 而这道题目还用到了前天的“未持有”的状态，一共用到三种状态，所以这道题创建的额外空间个数为3，这里用pre0表示前天“未持有”的状态。 

        for p in prices:
            pre0, f0, f1 = f0, max(f0, f1 + p), max(f1, pre0 - p)
            # 这里必须并行赋值，因为并行赋值才能实现右边全部用旧值计算再赋给左边的预期效果。 
            # 如果用分行赋值，计算结果时就会出现f1用到的pre0已经保存了新值的情况。 
            # 这是一个我出现了错误的点。2025.12.18 00:22 

        return f0 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2025.12.18 00:21 