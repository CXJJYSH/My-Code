from cmath import inf
from functools import cache
from typing import List

# 2025.12.11 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [inf] * (amount + 1)
        f[0] = 0
        for x in coins:
            for c in range(x, amount + 1):
                f[c] = min(f[c], f[c - x] + 1)
        ans = f[amount] 
        return ans if ans < inf else -1 
    
# 2026.05.27 14:50 

# 递归 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache 

        def dfs(i, c):
            if i < 0:
                return 0 if c == 0 else inf 
            if c < coins[i]:
                return dfs(i - 1, c)
            return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1) 
        
        ans = dfs(len(coins) - 1, amount)

        return ans if ans < inf else -1 
    
# 理解边界条件可以举coins = [7]，amount = 5的例子。 

# 时间复杂度O(n * amount) 
# 空间复杂度O(n * amount) 

# 2026.05.27 14:58 

# 循环 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins) 
        f = [[inf] * (amount + 1) for _ in range(n + 1)]
        f[0][0] = 0

        for i, x in enumerate(coins):
            for c in range(amount + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = min(f[i][c], f[i + 1][c - x] + 1)
        
        ans = f[n][amount]

        return ans if ans < inf else -1 
    
# 时间复杂度O(n * amount) 
# 空间复杂度O(n * amount) 

# 两种空间优化我现在就不写了，之后有时间再来写。 

# 题解链接：https://leetcode.cn/problems/coin-change/solutions/2119065/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-21m5/?envType=study-plan-v2&envId=top-100-liked 

# 2026.05.27 15:07 