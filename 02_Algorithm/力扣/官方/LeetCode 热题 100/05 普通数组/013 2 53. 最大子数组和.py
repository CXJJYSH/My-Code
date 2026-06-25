from cmath import inf
from typing import List

# 前缀和写法 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf 
        
        min_pre_sum = 0
        
        pre_sum = 0
        for x in nums: 
            pre_sum += x # 当前前缀和，卖出价格。 
        
            ans = max(ans, pre_sum - min_pre_sum) # 更新答案。 
            min_pre_sum = min(min_pre_sum, pre_sum) # 更新最小前缀和，当前前缀和已经当作卖出价格用完了，所以可以当作买入价格。 
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.16 11:42 

# 动态规划写法 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        f = [0] * len(nums) # 创建动态规划需要用到的记录数据结构。 
        
        f[0] = nums[0] # 初始化最开始不能用前面数据动态规划的元素。 
        
        for i in range(1, len(nums)):
            f[i] = max(f[i - 1], 0) + nums[i] # 逐个动态规划，完全符合索引。 
        
        return max(f) 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 动态规划空间优化写法 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf 
        
        f = 0

        for x in nums: 
            f = max(f, 0) + x 
            ans = max(ans, f)
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.16 12:16 

# 2026.06.25 15:08 

# 前缀和 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf 

        min_pre_sum = 0
        pre_sum = 0
        
        for x in nums:
            pre_sum += x
            ans = max(ans, pre_sum - min_pre_sum)
            min_pre_sum = min(min_pre_sum, pre_sum)
        
        return ans 
    
# 2026.06.25 15:09 