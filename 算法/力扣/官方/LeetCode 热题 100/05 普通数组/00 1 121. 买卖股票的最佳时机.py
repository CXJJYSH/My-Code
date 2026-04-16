from typing import List

# 枚举卖出价格，同时维护最低买入价格。 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]
        for p in prices: 
            ans = max(ans, p - min_price)
            min_price = min(min_price, p)
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.16 11:36 