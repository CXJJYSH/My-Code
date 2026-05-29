from cmath import inf
from functools import cache
from typing import List

# 递归写法 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        @cache 
        
        def dfs(i, c):
            if i < 0:
                return 0 if c == 0 else inf # 不合法的情况返回inf之后min取最小值的时候自然不会取不合法的答案。 
            
            if c < coins[i]:
                return dfs(i - 1, c)
            
            return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1) # 因为可以重复取，所以取完了该元素之后还能再取，只需要进行递归即可。 
        
        ans = dfs(n - 1, amount)
        
        return ans if ans < inf else -1 # 最后判断答案合法才进行返回，不合法则返回-1。 
    
# 时间复杂度O(n * amount)，i的取值范围是0到n = len(coins) - 1，c的取值范围是0到amount，总状态数为n * (amount + 1)，简化为n * amount， 
# 每个状态计算花费时间为O(1)，所以时间复杂度是O(n * amount) 
# 空间复杂度O(n * amount)， 状态数表示为O(n * amount)，每个状态只存一个整数值O(1)， 
# 而递归深度因为记忆化最多是O(n)或O(amount)，比较之后空间复杂度为O(n * amount)。 

# 总状态数的计算技巧就是直接看递归参数的取值范围，总状态数的个数就是范围相乘，再把常数简化。 

# 2025.12.11 16:25 

# 记忆化搜索转化成递推 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        
        f = [[inf] * (amount + 1) for _ in range(n + 1)] 
        # 这里是看递归函数的参数判断维度，这里就是i代表第一维度，c代表第二维度，分别用相应的取值范围进行初始化。 
        # i对应n，c对应amount，越小单位的索引其维度数越小，这里是越靠前编写。 
        f[0][0] = 0
        
        for i, x in enumerate(coins):
            for c in range(amount + 1):
                if c < x:
                    f[i + 1][c] = f[i][c] 
                else:
                    f[i + 1][c] = min(f[i][c], f[i + 1][c - x] + 1)
        
        ans = f[n][amount] 
        return ans if ans < inf else -1 
    
# 2025.12.11 17:17 

# 递推空间优化为一个数组的写法 

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
    
# 时间复杂度O(n * amount) 
# 空间复杂度O(amount) 

# 2025.12.11 17:30 