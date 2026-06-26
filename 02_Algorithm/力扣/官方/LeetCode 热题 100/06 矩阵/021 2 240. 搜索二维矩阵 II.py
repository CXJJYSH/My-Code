from typing import List

# 从右上角中间值元素开始查找，如果小了就增加行数，如果大了就减小列数，如果等于就返回True，没找到就循环结束返回False。 

# 也可以从左下角开始，只是小了就加列数，大了就减行数。 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = n - 1

        while i < m and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else: 
                return True 
        
        return False 
    
# 时间复杂度O(m + n)，最坏情况下这种方法从右上角元素开始一直往左，到了左上角时一直往下到左下角结束。 
# 空间复杂度O(1) 

# 2026.04.20 12:12 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])  
        
        i, j = 0, n - 1

        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True 
            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1
        
        return False 
    
# 时间复杂度O(m * n) 
# 空间复杂度O(1) 

# 2026.06.26 22:56 