from typing import List

# 2025.12.01 

MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        ans = []
        path = [""] * n 
        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return 
            for c in MAPPING[int(digits[i])]:
                path[i] = c 
                dfs(i + 1)
        dfs(0)
        return ans 
    
# 2026.05.13 12:51 

MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []

        ans = []
        path = [''] * n 

        def dfs(i):
            if i == n:
                ans.append(''.join(path))
                return 
            for c in MAPPING[int(digits[i])]:
                path[i] = c 
                dfs(i + 1) 

        dfs(0) 
        return ans 
    
# OK，拿捏。 

# 时间复杂度O(n * (4 ** n))，每次最多枚举4个字母，递归深度最多为n，所以递归时间O(4 ** n)，每次加入答案复制path需要O(n)，所以总体O(n * (4 ** n))。 
# 空间复杂度O(n)，返回值的空间不计入。 

# 2026.05.13 12:59 