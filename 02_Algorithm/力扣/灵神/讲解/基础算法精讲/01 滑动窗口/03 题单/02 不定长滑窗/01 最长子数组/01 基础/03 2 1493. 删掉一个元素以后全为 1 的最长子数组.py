from typing import List

# 我的代码 

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        cnt = 0
        
        for right, x in enumerate(nums):
            if x == 0:
                cnt += 1
            
            while cnt > 1:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans - 1 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.03 17:54 

# 灵神的代码 

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = cnt0 = left = 0

        for right, x in enumerate(nums):
            cnt0 += 1 - x
            # 这里在元素只有1和0的时候用到的计数方法是个很好的技巧，在写代码时可以省略if判断语句的书写，非常简洁有效。 
            # 直接用1减当前元素值，当前元素是0就记1，当前元素是1就记0，非常简洁有效。 
            
            while cnt0 > 1:
                cnt0 -= 1 - nums[left]
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans - 1 
    
# 时间复杂度O(n)，因为内层循环中对left的加一操作总数不会超过n，所以总的时间复杂度是O(n)。 
# 空间复杂度O(1) 

# 2026.01.03 18:02 