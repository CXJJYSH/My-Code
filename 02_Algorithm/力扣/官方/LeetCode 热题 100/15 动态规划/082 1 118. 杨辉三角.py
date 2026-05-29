from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        c = [[1] * (i + 1) for i in range(numRows)]
        for i in range(2, numRows):
            for j in range(1, i):
                c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
        return c 
    
# 时间复杂度O(n ** 2)，n == numRows。 
# 空间复杂度O(1) 

# 2026.05.26 12:12 