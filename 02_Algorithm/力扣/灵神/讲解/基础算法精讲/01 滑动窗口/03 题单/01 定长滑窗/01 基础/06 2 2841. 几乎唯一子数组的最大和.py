from collections import defaultdict
from typing import List

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        ans = 0 
        s = 0
        cnt = defaultdict(int)
        # 关键在于这里用字典初始化记录子数组元素的cnt，之后就能方便地用键值对统计子数组中各个元素的个数。 

        for i, x in enumerate(nums):
            s += x
            cnt[x] += 1
            
            left = i - k + 1 # 用新变量保存表达式的值有助于代码的书写美观，也更便于书写。 
            if left < 0:
                continue
            
            if len(cnt) >= m:
                ans = max(ans, s)
            
            out = nums[left] # 这里的out也是为了使代码更美观和更便于书写而设置的。 
            s -= out
            cnt[out] -= 1
            
            if cnt[out] == 0:
                del cnt[out]
        
        return ans 
    
# 时间复杂度O(n)，n为nums的长度。 
# 空间复杂度O(k)，k为子数组长度，计数字典占用的额外空间最多为子数组长度。 

# 2026.01.02 18:23 