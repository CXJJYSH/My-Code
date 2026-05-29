from typing import List

# 这道题用到的技巧是按特定顺序合并两个数组时，大的先从末尾往前排，两个给定数组和一个结果数组一共三个指针，这种不会覆盖为合并的元素。 

# 看了灵神的题解后我写出来的代码。 

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) 
        
        left = 0
        right = len(nums) - 1
        
        p = len(nums) - 1
        
        while p >= 0:
            x = nums[left] ** 2
            y = nums[right] ** 2
        
            if x > y:
                ans[p] = x
                p -= 1
                left += 1
            else:
                ans[p] = y
                p -= 1
                right -= 1
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.03.16 23:32 

# 灵神的写法，用的for循环，我用的while循环， 

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) 
        
        left = 0
        right = len(nums) - 1
        p = len(nums) - 1
        
        for p in range(len(nums) - 1, -1, -1):
            x = nums[left] ** 2
            y = nums[right] ** 2
        
            if x > y:
                ans[p] = x
                left += 1
            else:
                ans[p] = y
                right -= 1
        
        return ans 
    
# 灵神的另一种写法，只用计算一次乘法。 

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) 
        
        left = 0
        right = len(nums) - 1
        
        p = len(nums) - 1
        
        for p in range(len(nums) - 1, -1, -1):
            x = nums[left]
            y = nums[right]
        
            if -x > y:
                ans[p] = x * x
                left += 1
            else:
                ans[p] = y * y
                right -= 1
        
        return ans 
        
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.03.16 23:37 

# 2026.03.16 23:40 