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

# 递推写法 

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        f = [[[-inf] * 2 for _ in range(k + 2)] for _ in range(n + 1)]
        # 这里j维度用k + 2的原因是递归写法中j的取值范围为0到k，一共k + 1个元素，现在为了防止负数下标统一右移了一位，所以总数变为k + 2。 
        for j in range(1, k + 2):
            f[0][j][0] = 0
        # 这里要限制j的取值范围进行初始化的原因是递归时的边界条件时j == -1的时候不合法，递推统一右移一位导致j == 0时不合法， 
        # 合法的范围就是1到k + 1，所以代码写成range(1, k + 2)。 
        
        for i, p in enumerate(prices):
            for j in range(1, k + 2):
                f[i + 1][j][0] = max(f[i][j][0], f[i][j - 1][1] + p)
                f[i + 1][j][1] = max(f[i][j][1], f[i][j][0] - p)
        
        return f[n][k + 1][0] 
        # 最后范围因为统一右移，导致下标n - 1变为n，下标k变为k + 1，下标0代表False，表示未持有的状态。 

# 领悟：之后将记忆化搜索转化为递推的时候要先明确递归写法中各参数的边界条件，然后为了防止负数下标对范围进行相应调整， 
# 这样边界条件也会随着调整，这时候再在递推写法中根据正确的边界条件写出相应的代码。 
# 可能在初始化和循环遍历中也有相应的范围限制。 

# 时间复杂度O(nk) 
# 空间复杂度O(nk) 

# 2025.12.18 18:44 

# 递推写法空间优化

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        f = [[-inf] * 2 for _ in range(k + 2)]
        for j in range(1, k + 2):
            f[j][0] = 0

        for p in prices:
            for j in range(k + 1, 0, -1): # 这里的倒序遍历太灵动了，我自己写哪里想得到这里顺序遍历会出问题必须倒序遍历。 
                f[j][1] = max(f[j][1], f[j][0] - p)
                f[j][0] = max(f[j][0], f[j - 1][1] + p)
                # 还有这里，灵神可能考虑了分行赋值使用新旧值的问题，如果和之前的顺序一样结果可能会出错。 
                # 所以他将两条语句调换了一下顺序，这样就不存在本应该用旧值实际上却用了新值的情况了。 
                # 用并行赋值也是可以的，已经在力扣上试验过了。https://mubu.com/app/edit/home/3kOSbaToNgj  
                # 2025.12.18 19:31 
        
        return f[k + 1][0] 
    
# 太强了，灵神简直是天才。 

# 时间复杂度O(nk) 
# 空间复杂度O(k) 

# 2025.12.18 18:58 

# “恰好k次”和“至少k次”的代码就是要明确“恰好0次”和“至少0次”的时候结果是多少，然后再进行对应的边界条件初始化， 
# 这样之后进行递归，不管k的值是多少，都能递归出正确的结果，最后只要返回k对应的那个状态即可。  
# 难点就在初始化边界条件这里。 

# 想对多种情况进行练习、或重温代码，可以通过这个链接查看灵神的题解，再去对应的题目进行练习。 
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/solutions/2201488/shi-pin-jiao-ni-yi-bu-bu-si-kao-dong-tai-kksg/ 

# 2025.12.18 19:47 