from typing import List

# 空间复杂度O(m + n)的写法 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row_has_zero = [0 in row for row in matrix]
        col_has_zero = [0 in col for col in zip(*matrix)] # *matrix将matrix解包成行，给zip打包成元组，再存放在列表里。 

        for i, row_0 in enumerate(row_has_zero):
            for j, col_0 in enumerate(col_has_zero):
                if row_0 or col_0: # 如果这一元素所在的行或列有0，则将其置为0。 
                    matrix[i][j] = 0 

# 时间复杂度O(m * n)，创建row_has_zero和col_has_zero时分别进行了两次遍历。 
# 空间复杂度O(m + n) 

# 2026.04.17 12:22 

# 第一行第一列单独遍历的写法 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])

        first_row_has_zero = 0 in matrix[0]
        first_col_has_zero = any(row[0] == 0 for row in matrix)

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

        if first_col_has_zero:
            for row in matrix:
                row[0] = 0

# 时间复杂度O(m * n) 
# 空间复杂度O(1) 

# 2026.04.17 14:02 

# 只有第一行不进行遍历，最后先改第一列再改第一行。 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])

        first_row_has_zero = 0 in matrix[0]

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for row in matrix: 
                row[0] = 0 

        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

# 随着循环修改第一列的写法 

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m = len(matrix)
        n = len(matrix[0])

        first_row_has_zero = 0 in matrix[0]

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, m):
            for j in range(n - 1, -1, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0

# 时间复杂度O(m * n) 
# 空间复杂度O(1) 

# 还是第一种写法第一行和第一列单独修改的方法更容易懂和记住，而且比使用额外数组的方法优雅。 

# 2026.04.17 14:35 