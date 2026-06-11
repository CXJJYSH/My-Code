from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = cnt = 0
        for x in nums:
            if x:
                cnt += 1
                ans = max(ans, cnt) 
            else:
                cnt = 0
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.05.29 12:13 