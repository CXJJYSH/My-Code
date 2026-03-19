from typing import List

# 之前我写的代码。 

# 2025.10.14 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #时间复杂度O(n)
        #空间复杂度O(1)
        left = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                break
            if numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]
    
# 第二次我自己写的代码 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        
        left = 0
        right = len(numbers) - 1
        
        while left < right: 
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else: 
                ans.append(left + 1)
                ans.append(right + 1)
                break 
    
        return ans 

# 第二次我自己写的代码和第一次写的思路是一样的。 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.03.19 10:20 