from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = hp = 0

        for x in nums:
            if hp == 0:
                ans, hp = x, 1
            else:
                hp += 1 if x == ans else -1

        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.06.01 18:46 