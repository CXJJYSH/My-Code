from functools import cache

# 2025.12.12 

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        f[0] = list(range(m + 1))
        for i, x in enumerate(word1):
            f[i + 1][0] = i + 1
            for j, y in enumerate(word2):
                if x == y:
                    f[i + 1][j + 1] = f[i][j]
                else:
                    f[i + 1][j + 1] = min(f[i][j + 1], f[i + 1][j], f[i][j]) + 1
        return f[n][m] 
    
# 2026.05.30 16:34 

class Solution:
    def minDistance(self, s: str, t: str) -> int:
        m, n = len(s), len(t) 

        @cache 
        def dfs(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1
            if s[i] == t[j]:
                return dfs(i - 1, j - 1) 
            return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1 
            # 删除，插入，替换。 
            # 删除是删除当前i的字符，i - 1， 
            # 插入是在当前i后面添加字符，和当前j匹配，相当于让j的匹配情况减少1， 
            # 替换是替换当前i字符，然后i和j要匹配的字符同时减少1。 
            # 删除使结果字符串字符数减少1， 
            # 插入使结果字符串字符数增加1， 
            # 替换不改变字符串字符数。 
        
        return dfs(m - 1, n - 1)  
    
# 时间复杂度O(m * n) 
# 空间复杂度O(m * n) 

# 2026.05.30 17:01 

# 循环和优化之后再说。 
# https://leetcode.cn/problems/edit-distance/solutions/2133222/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-uo5q/?envType=study-plan-v2&envId=top-100-liked 

# 2026.05.30 17:01 

# 2026.05.31 今天考了信号与系统和软件工程导论。考完就去玩了，没写代码。 

# 2026.05.31 23:27 