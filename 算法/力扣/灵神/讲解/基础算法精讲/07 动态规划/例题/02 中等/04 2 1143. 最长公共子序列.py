from functools import cache

# 记忆化搜索写法 

# 运用“选或不选”思想，并运用数学功夫推理出可以直接排除的情况，简化代码。 

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1) 
        m = len(text2)

        @cache
        
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            
            if text1[i] == text2[j]:
                return dfs(i - 1, j - 1) + 1
            
            return max(dfs(i - 1, j), dfs(i, j - 1))
        
        return dfs(n - 1, m - 1)
    
# 时间复杂度O(nm) 
# 空间复杂度O(nm) 
# 总状态数为取值范围n * m 

# 递推写法 

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        f = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i, x in enumerate(text1):
            for j, y in enumerate(text2):
                if x == y:
                    f[i + 1][j + 1] = f[i][j] + 1
                else:
                    f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
        
        return f[n][m] 
    
# 套模板现在倒是套得挺快的，也没有什么问题了。 

# 时间复杂度O(nm) 
# 空间复杂度O(nm) 

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
    
# 空间优化：一个数组 
# 连续抽象相等的两行抽象判断位置关系 

# 时间复杂度O(nm) 
# 空间复杂度O(m)，去掉了n那个维度。 

# 2025.12.12 17:37 