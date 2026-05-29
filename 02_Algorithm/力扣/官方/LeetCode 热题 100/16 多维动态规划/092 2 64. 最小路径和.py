from cmath import inf
from functools import cache
from typing import List

# 递归 

# 没用@cache就超时了 

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache

        def dfs(i, j):
            if i < 0 or j < 0:
                return inf 
            if i == 0 and j == 0:
                return grid[i][j]
            return min(dfs(i - 1, j), dfs(i, j - 1)) + grid[i][j]

        return dfs(len(grid) - 1, len(grid[0]) - 1) 
    
# 时间复杂度O(m + n) 
# 空间复杂度O(m + n) 

# 2026.05.29 14:33 

# 循环和空间优化之后再说。 
# https://leetcode.cn/problems/minimum-path-sum/solutions/3045828/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-zfb2/?envType=study-plan-v2&envId=top-100-liked 

# 2026.05.29 14:34 