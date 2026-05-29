from functools import cache
from typing import List

# 递归 

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len = max(map(len, wordDict))
        words = set(wordDict) 

        @cache 
        def dfs(i):
            if i == 0:
                return True 
            for j in range(i - 1, max(i - max_len - 1, -1), -1):
                if s[j:i] in words and dfs(j):
                    return True 
            return False 
        
        return dfs(len(s)) 
    
# 时间复杂度O(m * L + n * (L ** 2)) 
# 空间复杂度O(m * L + n) 

# 2026.05.27 15:44 

# 循环 

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        max_len = max(map(len, wordDict))
        words = set(wordDict) 

        n = len(s) 
        f = [True] + [False] * n 
        for i in range(1, n + 1):
            for j in range(i - 1, max(i - max_len - 1, -1), -1):
                if s[j:i]in words and f[j]:
                    f[i] = True 

        return f[n] 
    
# f中可能有些元素二层循环结束后都没有置为True，但是最后到f[n]可能可以置为True。 

# 时间复杂度O(m * L + n * (L ** 2)) 
# 空间复杂度O(m * L + n) 

# 2026.05.27 15:49 

# 灵神也没写空间优化。 

# 复杂度还需要理解。 

# 2026.05.27 15:50 