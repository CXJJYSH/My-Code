from typing import List

# 方法一：从输入的视角————当前元素后面是否选择插入逗号。 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # 注意 s[n−1] 一定是最后一个字符，所以在 i=n−1 的时候一定要分割。
        
        ans = []
        path = []
        n = len(s)
        
        # 考虑 i 后面的逗号怎么选
        # start 表示当前这段回文子串的开始位置
        def dfs(i, start):
            if i == n:
                ans.append(path.copy())
                return 
            
            if i < n - 1:
                dfs(i + 1, start)
            # 这里本来直接dfs(i + 1, start)就可以了，但是i = n - 1的时候必须分割，如果没有if判断则代码执行会有错误。 
            # 这里是从判断“i之后的逗号要不要选”变成了判断“i + 1之后的逗号要不要选”。
            # 这里的start没变是因为没有分割，当前回文子串的开始位置和上一个递归中的回文子串的开始位置相同。

            t = s[start: i + 1]
            # 将字符串分割出开始位置为当前start，结束位置为i的子串，再判断是否为回文子串。 
            if t == t[::-1]:
                path.append(t)
                dfs(i + 1, i + 1)
                # 这里因为分割了，所以判断逗号的位置后移一位到了i + 1，start也变成了i + 1。 
                path.pop()
                # “修改——恢复”操作。 
        dfs(0, 0)
        return ans 
    
# 时间复杂度O(n * (2 ^ n)) 
# 空间复杂度O(n) 

# 中等 

# 2025.12.02 12:10 
    
# 方法二：从答案的视角————在当前元素之后找当前子串结束的位置。 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        n = len(s)
        
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return 
            for j in range(i, n):
                t = s[i: j + 1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j + 1)
                    path.pop()
        # 每次寻找子串结束的位置，然后判断，若有效则在结束位置之后进行递归。 
        # 灵神这里就是直接找子串结束的地方。 

        dfs(0)
        
        return ans 
    
# 时间复杂度O(n * (2 ^ n))，最久情况下。 
# 空间复杂度O(n)。 

# 中等 

# 2025.12.02 11:50 