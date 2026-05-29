from functools import cache

# 递归 

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache 
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if i == 0 and j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)
        return dfs(m - 1, n - 1)
    
# 时间复杂度O(m * n) 
# 空间复杂度O(m * n) 

# 2026.05.29 12:18 

# 还有循环和组合数学的做法，还有有障碍物的拓展题，这些都之后再来做吧。 
# https://leetcode.cn/problems/unique-paths/solutions/3062432/liang-chong-fang-fa-dong-tai-gui-hua-zu-o5k32/?envType=study-plan-v2&envId=top-100-liked 

# 2026.05.29 12:20 