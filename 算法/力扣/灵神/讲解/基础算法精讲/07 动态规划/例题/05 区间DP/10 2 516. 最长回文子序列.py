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

# 递推写法 

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        f = [[0] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            # 因为要从i + 1的情况转移到i，要先把i + 1算出来，所以到倒序遍历i。 

            f[i][i] = 1
            
            for j in range(i + 1, n):
                # 因为要从j - 1的情况转移到j，要先把j - 1算出来，所以要正序遍历j。 

                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
        
        return f[0][n - 1] 
    
# 时间复杂度O(n ^ 2) 
# 空间复杂度O(n ^ 2) 

# 2025.12.19 17:50 

# 递推写法空间优化

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        f = [0] * n
        
        for i in range(n - 1, -1, -1):
            # 倒序遍历的原因同上。 

            f[i] = 1
            pre = 0 # 初始值相当于f[i + 1][i]。 
            
            for j in range(i + 1, n):
                # 正序遍历的原因同上。 

                tmp = f[j] 
                f[j] = pre + 2 if s[i] == s[j] else max(f[j], f[j - 1])
                pre = tmp 
                # 这里因为f[j]对应的状态可能是f[i][j]、也可能是f[i + 1][j]，要准确地保存新旧数据，所以要用到中间变量暂存。  

        return f[-1] # 最后返回数组最后一个元素。 
    
# 时间复杂度O(n ^ 2) 
# 空间复杂度O(n) 

# 2025.12.19 18:03 

# 递推写法空间优化中用并行赋值也可以。 

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        
        f = [0] * n
        
        for i in range(n - 1, -1, -1):
            # 倒序遍历的原因同上。 

            f[i] = 1
            pre = 0 # 初始值相当于f[i + 1][i]。 

            for j in range(i + 1, n):
                # 正序遍历的原因同上。 

                f[j], pre= pre + 2 if s[i] == s[j] else max(f[j], f[j - 1]), f[j]
                # 并行赋值也没错。 

        return f[-1] # 最后返回数组最后一个元素。 
    
# 时间复杂度O(n ^ 2) 
# 空间复杂度O(n) 

# 2025.12.19 18:05 