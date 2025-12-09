from functools import cache
from typing import List

# 0-1背包 代码 

# capacity：背包容量 
# w[i]：第 i 个物品的体积 
# v[i]：第 i 个物品的价值 
# 返回：所选物品体积和不超过capacity的前提下，所能得到的最大价值和。 

def zero_one_knapsack(capacity, w, v):
    n = len(w)
    
    @cache 

    def dfs(i, c):
        if i < 0:
            return 0 
        
        if c < w[i]:
            return dfs(i - 1, c)
        
        return max(dfs(i - 1, c), dfs(i - 1, c - w[i]) + v[i])
    
    return dfs(n - 1, capacity)

# 494.目标和 代码 

# 记忆化搜索 
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)

        if target < 0 or target % 2:
            return 0
        
        target //= 2
        
        # 下面是套用0-1背包模板 

        n = len(nums)
        
        @cache
        
        def dfs(i, c):
            if i < 0:
                return 1 if c == 0 else 0
            
            if c < nums[i]:
                return dfs(i - 1, c)
            
            return dfs(i - 1, c) + dfs(i - 1, c - nums[i])
        
        return dfs(n - 1, target) 
    
# 原理推导 
# 前加加号的元素和设为p， 
# 所有元素和设为s， 
# 前加减号的元素和则为s-p， 
# 则 p - (s - p) = target 
# target = 2p - s
# 2p = target + s 
# p = (target + s) // 2
# 因为所给元素都为 非负数 
# 所以 target + s >= 0 且 (target + s) % 2 == 0 
# 最后问题转化为求“所选元素和恰好为转化式的方案个数” 
# 这样就转化为了“选或不选”问题。 

# 时间复杂度O(nm) 
# 空间复杂度O(nm) 
# 详情见 https://leetcode.cn/problems/target-sum/solutions/2119041/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-s1cx/ 

# 2025.12.09 17:10 

# 递推 

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)

        if target < 0 or target % 2:
            return 0
        
        target //= 2
        
        n = len(nums)
        
        f = [[0] * (target + 1) for _ in range(n + 1)] 
        # target + 1是为了让后面能索引到target，n + 1是防止出现负数索引提前加一的对应结果，最后一个元素的索引为n。 
        
        f[0][0] = 1 # 这里是一比一翻译递归的边界条件，是经过边界调整之后的边界条件翻译的结果。 
        
        for i, x in enumerate(nums):
            for c in range(target + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = f[i][c] + f[i][c - x] # 这里就是边界调整之后的计算公式。 
        
        return f[n][target]         