from functools import cache

# 记忆化搜索写法 

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        @cache 
        
        def dfs(i, j):
            # 通过判断区间头尾两元素是否都选来进行区间缩小，都选的话区间两头索引向内缩一， 
            # 不能都选的话就头往内缩一或尾往内缩一，再取最大值。 

            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return dfs(i + 1, j - 1) + 2
            return max(dfs(i + 1, j), dfs(i, j - 1))
        
        return dfs(0, n - 1)
    
# 总状态数O(n ^ 2)，每个状态计算时间都为O(1)，所以 
# 时间复杂度O(n ^ 2) 
# 空间复杂度O(n ^ 2) 

# 2025.12.19 17:37 