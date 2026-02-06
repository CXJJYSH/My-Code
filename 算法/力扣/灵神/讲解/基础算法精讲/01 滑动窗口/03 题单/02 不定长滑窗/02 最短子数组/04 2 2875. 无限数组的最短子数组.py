from cmath import inf
from typing import List

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        rem = target % total 
        
        n = len(nums)
        ans = inf
        left = 0
        s = 0
        
        for right in range(n * 2):
            s += nums[right % n]
            
            while s > rem:
                s -= nums[left % n]
                left += 1
            
            if s == rem:
                ans = min(ans, right - left + 1)
        
        return ans + target // total * n if ans < inf else -1 
    
# 我自己一开始没想出来能完全通过的写法，后来去看了灵神的题解才通过的。 
    
# 这里灵神很巧妙地将target拆分成了nums数组和的整数倍加一个小于nums数组和的数，和用total表示，余数用rem表示。 
# 最开始用sum()和取模运算表示出total和rem。 
# 因为拆分成了两个部分，和部分可以直接剔除，所以只用看两个nums数组连续构成的新数组中能不能用滑动窗口找到长度最小的和为rem的子数组。 
# 如果能找到，则结果用子数组长度加上nums数组长度的整数倍表示。 
# 如果找不到则返回-1。 
# 最后用if-else语句判断是否找到。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.08 23:56 