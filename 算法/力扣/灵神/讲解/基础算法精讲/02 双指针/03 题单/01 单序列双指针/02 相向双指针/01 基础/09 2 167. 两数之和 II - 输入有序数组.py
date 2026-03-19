from typing import List

# 灵神解释的本题要点 
# ⚠注意： 
# 虽然题目说下标从 1 开始，但输入的 numbers 数组的下标仍然是从 0 开始的。我们应当按照从 0 开始的下标写代码，只是在最后返回的时候，把下标加一。

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

# 灵神的写法 

# 时间击败率都是一样的。灵神的还是更简洁一点。 

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while True:
            s = numbers[left] + numbers[right] 
        
            if s == target:
                return [left + 1, right + 1]
            elif s > target:
                right -= 1
            else: 
                left += 1

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.03.19 10:45 