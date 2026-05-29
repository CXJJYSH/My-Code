from typing import List


class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        ans = []
        
        n = len(arr) 
        arr.sort()
        m = arr[(n - 1) // 2]
        
        left = 0
        right = n - 1
        
        while left <= right:
            if abs(arr[left] - m) > abs(arr[right] - m):
                ans.append(arr[left])
                left += 1
            elif abs(arr[left] - m) == abs(arr[right] - m) and arr[left] > arr[right]:
                ans.append(arr[left]) 
                left += 1
            else: 
                ans.append(arr[right]) 
                right -= 1
        
        return ans[0 : k]
    
# 我也不知道我一开始的写法错在哪了，现在的写法是从强到弱排序之后返回最前面k个元素，排序过程中左右指针从两遍向中间靠拢，这样就没有错了。 

# 时间复杂度O(n * log n) 
# 空间复杂度O(1) 

# 2026.03.18 11:04 

# 看了灵神学生的题解之后发现删了 elif 那一句也可以得到正确答案，因为排序后不存在左边元素大于右边元素的情况，不影响正确性。 

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        ans = []

        n = len(arr) 
        arr.sort()
        m = arr[(n - 1) // 2]
        
        left = 0
        right = n - 1
        
        while left <= right:
            if abs(arr[left] - m) > abs(arr[right] - m):
                ans.append(arr[left])
                left += 1
            else: 
                ans.append(arr[right]) 
                right -= 1
        
        return ans[0 : k]
    
# 时间复杂度O(n * log n) 
# 空间复杂度O(1) 

# 2026.03.18 11:29 