from typing import List

# 我的写法 

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - 1

        while right - left + 1 > k:
            if abs(arr[left] - x) < abs(arr[right] - x):
                right -= 1
            elif abs(arr[left] - x) == abs(arr[right] - x) and arr[left] < arr[right]:
                right -= 1
            # 根据题目条件可知只要不满足上述两种情况的就是b比a更接近的情况，这时移动左指针即可。 
            else:
                left += 1
        
        return arr[left : right + 1]

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.03.17 11:07 ~ 11:11 四分钟搞定。 

# 2026.03.17 11:12 

# 我感觉我的写法还是挺好的，没看到灵神的题解，我的写法比其他人的写法更快，我的35.09%，一个Python题解只有15.07%。还行。 

# 2026.03.17 11:17 