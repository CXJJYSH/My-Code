from typing import List

# 2025.12.02 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # 注意 s[n−1] 一定是最后一个字符，所以在 i=n−1 的时候一定要分割。
        ans = []
        path = []
        n = len(s)
        def dfs(i, start):
            if i == n:
                ans.append(path.copy())
                return 
            
            if i < n - 1:
                dfs(i + 1, start)

            t = s[start: i + 1]
            if t == t[::-1]:
                path.append(t)
                dfs(i + 1, i + 1)
                path.pop()
        dfs(0, 0)
        return ans 
    
# 2026.05.15 11:33 

# 选或不选 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s) 
        ans = []
        path = []

        def dfs(i, start):
            if i == n:
                ans.append(path.copy())
                return 
            
            # 不选s[i]作为切割点，直接往后递归。 
            if i < n - 1:
                dfs(i + 1, start)

            # 选s[i]作为切割点。 
            t = s[start : i + 1]
            if t == t[::-1]:
                path.append(t)
                dfs(i + 1, i + 1)
                path.pop()

            # 我感觉就应该把不选的情况放到选的后面去，这样读起来更容易懂一点。 

        dfs(0, 0)
        return ans 
    
# 时间复杂度O(n * (2 ** n))，一共 2 ** n 个节点，判断是否是回文串需要O(n)时间复杂度。 
# 空间复杂度O(n)，判断回文串时用的切片为O(n)空间复杂度。 

# 2026.05.15 11:44 

# 灵神选或不选注释 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        path = []

        # 现在 s 未被分割的部分为 [start, n-1]
        # 当前位于下标 i，讨论是否在 i 和 i+1 之间切一刀
        def dfs(i: int, start: int) -> None:
            if i == n:  # s 分割完毕
                ans.append(path.copy())  # 复制 path
                return

            # 不分割
            if i < n - 1:  # i=n-1 时必须分割（这是最后一段），i<n-1 时才可以不分割
                dfs(i + 1, start)

            # 分割，那么得到子串 [start, i]
            t = s[start: i + 1]
            if t == t[::-1]:  # 判断 t 是不是回文串
                path.append(t)
                # 现在 s 未被分割的部分为 [i+1, n-1]
                dfs(i + 1, i + 1)
                path.pop()  # 恢复现场

        dfs(0, 0)
        return ans 
    
# 枚举选哪个 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s) 
        ans = []
        path = []

        # 现在 s 未被分割的部分为 [i, n-1] 
        # 里面的for循环枚举下一刀切在哪 
        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return 
            
            for j in range(i, n):
                t = s[i : j + 1]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j + 1)
                    path.pop()

        dfs(0)
        return ans 
    
# 时间复杂度O(n * (2 ** n))，一共 2 ** n 个节点，判断是否是回文串需要O(n)时间复杂度。 
# 空间复杂度O(n)，判断回文串时用的切片为O(n)空间复杂度。 

# 2026.05.15 11:53 