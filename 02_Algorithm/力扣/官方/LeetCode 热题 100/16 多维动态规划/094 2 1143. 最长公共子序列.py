from functools import cache

# 2025.12.12 

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text2)
        
        f = [0] * (m + 1)
        
        for x in text1:
            pre = f[0] 
            for j, y in enumerate(text2):
                tmp = f[j + 1]
                
                f[j + 1] = pre + 1 if x == y else max(f[j + 1], f[j])
                
                pre = tmp 
        
        return f[m] 
    
# 2026.05.30 16:28 

# 递归 

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2) 

        @cache 
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if text1[i] == text2[j]:
                return dfs(i - 1, j - 1) + 1
            return max(dfs(i - 1, j), dfs(i, j - 1))
        
        return dfs(m - 1, n - 1) 
    
# 时间复杂度O(m * n) 
# 空间复杂度O(m * n) 

# 2026.05.30 16:33 

# 循环和优化之后再说。 
# https://leetcode.cn/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=top-100-liked 

# 2026.05.30 16:33 