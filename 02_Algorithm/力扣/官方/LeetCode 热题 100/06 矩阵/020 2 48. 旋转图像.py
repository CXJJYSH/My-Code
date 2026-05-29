from typing import List

# 第一种方法 

# 先转置，再行翻转。 

# 可以看成是枚举对角线下的元素，然后和对角线上的对称元素交换。 

# 转置过程可以堪称看成一个不断扩大的正方形。 

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

# 第二种方法 

# 从第一行开始逐步将后面的元素和目标元素进行交换，随着行数的增加，前面的元素自然都保存着正确的元素，不用特意交换。 

# 执行过程可以看成是以对角线元素为对称点，将对称点后面那一行的所有元素和对称点下面那一列的所有元素进行交换，可以看成未交换的元素组成了一个正方形。 

# 时间复杂度O(n ** 2) 
# 空间复杂度O(1) 

# 2026.04.20 11:58 