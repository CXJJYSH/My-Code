from cmath import inf
from typing import List

# 这段代码不知道为什么有时候不能找全答案 

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            if i < k:
                for j in range(min(i + k + 1, len(nums))):
                    if nums[j] == key and not j in ans: 
                        ans.append(j)
            else:
                for j in range(i - k, min(i + k + 1, len(nums))):
                    if nums[j] == key and not j in ans:
                        ans.append(j)
        return ans 
    
# MD，写了两遍这简单题都没写出来 

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        for i in range(len(nums)):
            left = max(i - k, 0)
            right= min(i + k, len(nums) - 1)
            for j in range(left, right + 1):
                if nums[j] == key and j not in ans:
                    ans.append(j)
        return ans 
    
# 滑动窗口写法 
# 记录key出现的最晚位置，看是否在滑动窗口内 

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        last = -inf 
        for i in range(k - 1, -1, -1):
            if nums[i] == key:
                last = i 
                break

        ans = []
        n = len(nums)
        for i in range(n):
            if i + k < n and nums[i + k] == key:
                last = i + k 
            if last >= i - k:
                ans.append(i)
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.09 23:14 

# 同向双指针写法 

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        
        j = 0
        for i, x in enumerate(nums):
            if x != key:
                continue 
        
            j = max(j, i - k)
        
            while j <= min(i + k, len(nums) - 1):
                ans.append(j) 
                j += 1
        
        return ans 
    
# 找key的索引 
# j保持在界内 
# j在不越界情况下加入ans 
# 加入完之后j在窗口最右端，可能大于下一个窗口左索引，此时j只会更新右端的新值，左端的索引不会重复加入，所以答案不会重复。 

# 时间复杂度O(n)，i和j都最多从左到右遍历一遍。 
# 空间复杂度O(1) 

# 2026.04.09 23:40 