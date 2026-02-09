from typing import List

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for j in range(y, y + k):
            left = x
            right = x + k - 1
            
            while left < right:
                grid[left][j], grid[right][j] = grid[right][j], grid[left][j]
                left += 1
                right -= 1
        
        return grid
    
# 牛逼，二维列表的区域反转一遍过，我真牛逼。 

# 最先要做的就是确定行和列的变量的范围。 
# 这是一列一列地交换的，所以最外层循环要用列作为变量。 
# left和right表示行。 
# +=和-=分别表示向下和向上的意思。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.02.09 16:17 

# 下面是灵神的写法 

class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        left = x 
        right = x + k - 1

        while left < right:
            for j in range(y, y + k):
                grid[left][j], grid[right][j] = grid[right][j], grid[left][j]
        
            left += 1
            right -= 1
        
        return grid 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 
    
# 灵神的写法是先确定行，然后逐个将这两行的所有元素进行反转。可以说是横着来的。 
# 我的写法是先确定列，然后逐个将这一列的所有元素进行反转。可以说是竖着来的。 

# 我的写法是先反转完的列，灵神的写法是先反转完的行。 

# 这两种写法都可以。 

# 还有一种确定行之后直接用切片反转的写法，但是这种写法就有O(k)的空间复杂度。 

# 2026.02.09 16:31 