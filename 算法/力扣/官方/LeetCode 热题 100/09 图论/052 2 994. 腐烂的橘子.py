from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0]) 

        fresh = 0
        q = [] 
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    fresh += 1
                elif x == 2:
                    q.append((i, j)) 

        ans = 0
        while q and fresh:
            ans += 1
            tmp = q 
            q = []
            for x, y in tmp:
                for i, j in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                    if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                        fresh -= 1
                        grid[i][j] = 2 
                        q.append((i, j))
        
        return -1 if fresh else ans 
    
# 时间复杂度O(m * n) 
# 空间复杂度O(m * n) 

# 2026.05.12 11:12 