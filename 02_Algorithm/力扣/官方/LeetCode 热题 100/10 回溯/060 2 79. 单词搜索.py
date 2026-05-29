from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            if board[i][j] != word[k]:
                return False 
        
            if k == len(word) - 1:
                return True 
        
            board[i][j] = ''
            for x, y in (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j):
                if 0 <= x < m and 0 <= y < n and dfs(x, y, k + 1):
                    return True 
            board[i][j] = word[k]
        
            return False 
        
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))
    
# 时间复杂度O(m * n * (3 ** length)) 
# 空间复杂度O(length)，length为字符串长度。 

# 没学优化写法，之后有机会再回来看吧。 
# https://leetcode.cn/problems/word-search/solutions/2927294/liang-ge-you-hua-rang-dai-ma-ji-bai-jie-g3mmm/?envType=study-plan-v2&envId=top-100-liked 

# 2026.05.15 11:31 