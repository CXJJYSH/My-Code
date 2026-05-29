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
        
        return f[n][target] # n是防止出现负数边界调整后的最后元素索引，target是表示目标的索引。 
    
# 2025.12.09 

# 改成递推后的空间优化一：用两个数组 

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        
        if target < 0 or target % 2:
            return 0
        
        target //= 2
        
        n = len(nums)
        
        f = [[0] * (target + 1) for _ in range(2)]
        f[0][0] = 1
        
        for i, x in enumerate(nums):
            for c in range(target + 1):
                if c < x:
                    f[(i + 1) % 2][c] = f[i % 2][c]
                else:
                    f[(i + 1) % 2][c] = f[i % 2][c] + f[i % 2][c - x]
        
        return f[n % 2][target] 
        
        # 所有与i或n有关的索引都模2。这样就能简化为在f[0]、f[1]两个数组上进行状态保存和更新。 

# 2025.12.10 16:38 

# 改成递推后的空间优化二：只用一个数组 

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        
        if target < 0 or target % 2:
            return 0
        
        target //= 2
        
        n = len(nums)
        
        f = [0] * (target + 1) # 空间优化二直接把第二个维度删了。 
        f[0] = 1
        
        for x in nums:
            for c in range(target, x - 1, -1): 
                # 这里的倒序遍历和之前的正序遍历的区别在于多了一个边界限制， 
                # 边界限制的原因是如果c小于了x，到了x - 1，那么c - x就会变成负数下标，导致程序出错。 
                # 所以限制边界只是为了防止越界这个问题。 
                if c < x:
                    f[c] = f[c]
                else:
                    f[c] = f[c] + f[c - x]
                # 然后上面的代码其实可以改成 
                # if c >= x: 
                #     f[c] = f[c] + f[c - x] 
                # 完整修改见下 
        
        return f[target] 
    
# 空间优化二完整修改 

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2:
            return 0
        target //= 2
        n = len(nums)
        f = [0] * (target + 1)
        f[0] = 1
        for x in nums:
            for c in range(target, x - 1, -1):
                if c >= x:
                    f[c] = f[c] + f[c - x]
        return f[target] 
    
# 2025.12.10 17:13 