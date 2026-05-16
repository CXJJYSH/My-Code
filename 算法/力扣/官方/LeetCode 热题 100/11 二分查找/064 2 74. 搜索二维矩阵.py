from typing import List

# 二分查找 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        left, right = -1, m * n 
        
        while left + 1 < right:
            mid = (left + right) // 2
        
            x = matrix[mid // n][mid % n]
        
            if x == target:
                return True 
        
            if x < target:
                left = mid 
            else:
                right = mid 
        
        return False 
    
# 时间复杂度O(log (m * n)) 
# 空间复杂度O(1) 
    
# 排除 

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
    
# 时间复杂度O(m + n) 
# 空间复杂度O(1) 

# 2026.05.16 12:01 