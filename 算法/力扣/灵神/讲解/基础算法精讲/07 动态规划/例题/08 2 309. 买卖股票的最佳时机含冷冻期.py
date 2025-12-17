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
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])
        
        return dfs(n - 1, False) 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2025.12.17 23:21 