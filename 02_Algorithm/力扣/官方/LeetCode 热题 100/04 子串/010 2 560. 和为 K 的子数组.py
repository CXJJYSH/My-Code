from collections import defaultdict
from typing import List

# 2026.02.03 前缀和写法 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = defaultdict(int) 
        s = 0
        for x in nums:
            cnt[s] += 1
            s += x 
            ans += cnt[s - k]
        return ans 
    
# 2026.04.14 12:48 前缀和写法 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        s = 0 # 前缀和 
        cnt = defaultdict(int) # 不同前缀和出现次数的统计字典 
        
        for x in nums:
            cnt[s] += 1 # 当前元素之前的元素和-即前缀和-数量加一 
            s += x # 更新为后一个元素的前缀和 
            ans += cnt[s - k] # 不知道为什么要在这里计算答案 
        
        return ans 

# 时间复杂度O(n)，nums长度。 
# 空间复杂度O(m)，字典长度。 

# 2026.04.14 12:54 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x 
        
        cnt = defaultdict(int) 
        ans = 0
        for sj in s:
            ans += cnt[sj - k]
            cnt[sj] += 1
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.06.11 16:28 