from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        cur_end = 0
        next_end = 0
        for i in range(len(nums) - 1):
            next_end = max(next_end, i + nums[i])
            if i == cur_end:
                cur_end = next_end
                ans += 1
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.05.25 12:36 

# 拿一个例子跟着代码试一下就懂为什么ans的更新方法可行了。也可以结合灵神题解。 

# 2026.05.25 12:40 