from cmath import inf
from functools import cache
from typing import List


# 记忆化搜索写法 

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        @cache
        
        def dfs(i, j, hold):
            if j < 0:
                return -inf 
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, j, True), dfs(i - 1, j, False) - prices[i])
                # 这是当天结束时“持有股票”的情况，可能存在的“买入”操作不算作影响交易次数的因素，所以买入相当于交易次数没有变化。 
            return max(dfs(i - 1, j, False), dfs(i - 1, j - 1, True) + prices[i])
            # 这是当天结束时“未持有股票”的情况，可能存在的“卖出”操作算作影响交易次数的因素，所以卖出相当于交易次数加一。 

            # 也可以将“买入”算作影响因素，“卖出”不算作，这样改动相应的代码仍然是对的。 
        
        return dfs(n - 1, k, False) 

# 时间复杂度O(nk) 
# 空间复杂度O(nk) 

# 2025.12.18 17:47 