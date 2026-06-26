from typing import List

# 标记写法 

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0)) # 我觉得这里写两层括号更好。 

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = 0
        di = 0 # 确定方向 

        for _ in range(m * n): # 一共遍历并记录m * n次 
            ans.append(matrix[i][j]) # 记录答案 

            matrix[i][j] = None  # 标记 

            x = i + DIRS[di][0]
            y = j + DIRS[di][1]
            # 这里只是模拟判断有没有越界或标记，不是真的改变了索引进行下一步。 

            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] is None:
                di = (di + 1) % 4 # 更新方向 

            i += DIRS[di][0]
            j += DIRS[di][1]
            # 更新索引 

        return ans # 返回答案 
    
# 时间复杂度O(m * n) 
# 空间复杂度O(1) 

# 2026.04.17 15:06 

# 不标记写法 

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        m = len(matrix)
        n = len(matrix[0])

        size = m * n 

        i = 0
        j = -1 
        di = 0
        # 设置起始位置和起始方向 

        while len(ans) < size:
            dx = DIRS[di][0]
            dy = DIRS[di][1]
            # 设定每一步各方向的步长 

            for _ in range(n): # 每次走n步，n会变。 
                i += dx 
                j += dy 
                ans.append(matrix[i][j]) # 初始位置不在矩阵里，所以要走完一步再记录。 

            di = (di + 1) % 4 # 更新方向 

            n, m = m - 1, n # 更新要走的步数 
        
        return ans 
    
# 时间复杂度O(m * n) 
# 空间复杂度O(1) 

# 2026.04.17 15:33 

DIRS = (0, 1), (1, 0), (0, -1), (-1, 0)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0]) 

        ans = []
        
        i = j = di = 0 
        
        for _ in range(m * n):
            ans.append(matrix[i][j])
        
            matrix[i][j] = None 
        
            x, y = i + DIRS[di][0], j + DIRS[di][1] 
        
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] is None:
                di = (di + 1) % 4
        
            i += DIRS[di][0]
            j += DIRS[di][1]
        
        return ans 
    
# 时间复杂度O(m * n) 
# 空间复杂度O(1) 

# 2026.06.26 21:58 