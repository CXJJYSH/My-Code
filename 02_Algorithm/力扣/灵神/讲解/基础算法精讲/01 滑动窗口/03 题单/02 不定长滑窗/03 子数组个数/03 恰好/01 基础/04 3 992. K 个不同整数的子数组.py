from collections import defaultdict
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def solve(k):
            ans = 0
            cnt = defaultdict(int) 
            left = 0

            for x in nums:
                cnt[x] += 1

                while len(cnt) >= k:
                    out = nums[left] 
                    cnt[out] -= 1
                    if cnt[out] == 0:
                        del cnt[out] 
                    left += 1

                ans += left 

            return ans

        return solve(k) - solve(k + 1)
    
# 虽然看着是困难题，但实际上是常规题，直接套用灵神思路写一个函数，最后调用两次就可以了。 
# 难度分数为2210的题目用对了方法都可以不看题解一次过了。 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.02.06 16:36 