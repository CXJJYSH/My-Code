from typing import Counter, List

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0
        cnt = Counter()
        left = 0
        
        for right, x in enumerate(nums):
            cnt[x] += 1
            
            while max(cnt) - min(cnt) > 2: # 这里用计数字典统计元素可以直接消去题目条件中的绝对值符号。 
                
                # 但是max和min内置函数需要用到O(n)时间复杂度。
                # 因为这里cnt的最大值已经知道是一个常数 2 + 1 = 3 了，所以用D表示最大值最小值之差的上限，则时间复杂度为O(D)。 
                # 灵神说是O(D)，但是我感觉是O(D + 1)。 

                out = nums[left] 
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
                left += 1
            
            ans += right - left + 1
        
        return ans 

# 时间复杂度O(n * D) / 时间复杂度O(n * (D + 1)) 
# 空间复杂度O(D) / 空间复杂度O(D + 1) 

# 2026.01.25 11:54 