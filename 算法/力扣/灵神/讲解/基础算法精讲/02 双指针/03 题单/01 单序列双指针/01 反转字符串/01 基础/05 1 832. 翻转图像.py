# OK，这道题也是在3分钟之内完成了。 
# 二维列表简单题。 

# 因为看到了数据数量范围在20及以内，所以就放心地采用了O(n ^ 2)时间复杂度的写法。 

from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        for i in range(n):
            left = 0
            right = n - 1
            while left < right:
                image[i][left], image[i][right] = image[i][right], image[i][left]
                left += 1
                right -= 1

        for i in range(n):
            for j in range(n):
                image[i][j] = 1 - image[i][j]

        return image 
    
# 时间复杂度O(n ^ 2) 
# 空间复杂度O(1) 

# 2026.02.10 11:35 