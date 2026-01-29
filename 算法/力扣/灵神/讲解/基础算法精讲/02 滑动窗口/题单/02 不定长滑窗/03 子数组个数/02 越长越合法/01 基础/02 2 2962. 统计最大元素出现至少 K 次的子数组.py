from collections import Counter
from typing import List

# 2025.10.26 提交的版本 

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # 我的代码超出时间限制了😢。写了二十多分钟，快三十分钟了。
        '''
        ans = 0
        max_value = max(nums)
        num = 0
        for right, i in enumerate(nums):
            left = 0
            if i == max_value:
                num += 1
            cnt = num
            while cnt >= k:
                ans += 1
                if nums[left] == max_value:
                    cnt -= 1
                left += 1
        return ans
        '''
        # 这是自己看了灵神的题解后自己写的代码。
        '''
        mx = max(nums)
        ans = 0
        cnt = 0
        left = 0
        for right, i in enumerate(nums):
            if i == mx:
                cnt += 1
            while cnt == k:
                if nums[left] == mx:
                    cnt -= 1
                left += 1
            ans += left
        return ans
        '''
        # 这是灵神的代码。
        mx = max(nums)
        ans = 0
        cnt = 0
        left = 0
        for i in nums:
            if i == mx:
                cnt += 1
            while cnt == k:
                if nums[left] == mx:
                    cnt -= 1
                left += 1
            ans += left
        return ans 
    
# 2026.01.29 的版本 

# 我自己写的代码，第二遍的代码，第一遍的统计成子数组中的最大元素了，好像还统计错了，第二遍才写对。 

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        mx = max(nums)
        cnt = Counter()
        left = 0

        for c in nums:
            cnt[c] += 1
            
            while cnt[mx] >= k:
                out = nums[left]
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
                left += 1
            
            ans += left
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.01.29 11:27 

# 灵神的代码 

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        mx = max(nums)
        cnt_mx = 0
        left = 0

        for c in nums:
            if c == mx:
                cnt_mx += 1
            
            while cnt_mx == k:
                if nums[left] == mx:
                    cnt_mx -= 1
                left += 1
            
            ans += left
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 从灵神的优化点可以领悟到 
# 当统计答案的时间点只由一个元素控制时，可以不创建占用额外空间的变量，直接用一个变量统计该单一元素的数据， 
# 这样空间复杂度就从O(n)优化到了O(1)。 

# 2026.01.29 11:32 