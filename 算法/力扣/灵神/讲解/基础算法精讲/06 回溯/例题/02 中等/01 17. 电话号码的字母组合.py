from typing import List

MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        # 先获取长度，若长度为0直接返回[]。

        ans = []
        path = [""] * n # "" 就是空字符串的意思。

        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return
            # 边界条件，合并path中记录的字符。
             
            for c in MAPPING[int(digits[i])]:
                path[i] = c 
                dfs(i + 1)
            # 非边界条件，按照题目给的条件在素材数组中找到对应的素材组，然后每一个单独的元素都有一个循环对应下一个递归，
            # 所以能保证回溯出所有应有的情况。

        dfs(0)
        # 最后从头开始递归，每一个i == n的末尾ans都记录了一个新的答案值。
        # 递归完ans中就是所有应有的答案。

        return ans 
        # 最后返回ans即可。

# 时间复杂度O(n * (4 ^ n))。
# 原因是对于给的长度为n的起始数组，有可能每一个指令都对应这4个字母，结合循环就有4 ^ n种情况（可以用高中学的排列组合来理解；
# 而我猜测灵神讲的生成答案的步骤时间复杂度为O(n)应该是指ans.append("".join(path))这一步，
# 而因为每种情况最后都要有一步生成答案，所以整体的时间复杂度是O(n * (4 ^ n))。

# 空间复杂度O(n)，我猜是指额外数组path用到了O(n)的额外变量。

# 中等

# 2025.12.01 16:52