# 这道题给的数组中的元素可能为负数。 

from collections import defaultdict
from typing import List

# 两次遍历 
# 先遍历一遍nums构建前缀和数组，再遍历前缀和数组计算答案。 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 构建前缀和数组。 

        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x
        
        # 计算有多少符合条件的数对。 

        ans = 0
        cnt = defaultdict(int)
        for j in s:
            ans += cnt[j - k] 
            cnt[j] += 1
        
        # 这里要先更新答案，然后再更新当前元素出现的个数。 
        # 因为之前的元素就算和当前元素值一样，也不应该计入答案总数里。 
        # 这里统计的是当前元素前可以和当前元素组成数对的历史元素。 

        return ans 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.02.03 16:53 

# 一次遍历 · 一 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0

        s = 0
        
        cnt = defaultdict(int) 
        cnt[0] = 1 
        
        for x in nums:
            s += x 
            ans += cnt[s - k]
            cnt[s] += 1
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.02.03 17:08 

# 一次遍历 · 其二 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        
        cnt = defaultdict(int) 
        s = 0
        
        for x in nums:
            cnt[s] += 1
            # 这里实际上统计的是上一个前缀和。 

            s += x 
            ans += cnt[s - k]
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(m)，m为不同前缀和的个数。一般来说是哈希表的容量O(n) 

# 2026.02.03 17:13 