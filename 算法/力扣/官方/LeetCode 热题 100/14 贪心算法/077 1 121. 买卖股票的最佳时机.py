# 加到个小红书好友，聊天和玩去了，今天上完毛概课后脑勺好痛，可能是因为低头太久了。

# 2026.05.22 23:42 

# 今天啥也没干说是，上午去做了个计组实验。。。

# 2026.05.23 23:38 

# 今天又是啥也没干，去玩了一天。 

# 2026.05.24 23:25 

from typing import List

# 2026.04.16 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]
        for p in prices: 
            ans = max(ans, p - min_price)
            min_price = min(min_price, p)
        return ans 
    
# 2026.05.25 11:09 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]
        for i in prices:
            ans = max(ans, i - min_price)
            min_price = min(i, min_price)
        return ans 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.05.25 11:11 