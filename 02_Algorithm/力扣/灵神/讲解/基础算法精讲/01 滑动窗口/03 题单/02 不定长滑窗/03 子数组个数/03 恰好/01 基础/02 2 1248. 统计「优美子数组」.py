from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def solve(k):
            ans = 0
            cnt = 0
            left = 0

            for x in nums:
                if x % 2 == 1:
                    cnt += 1

                while cnt >= k:
                    out = nums[left]
                    if out % 2 == 1:
                        cnt -= 1
                    left += 1

                ans += left 

            return ans 

        return solve(k) - solve(k + 1) 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.02.04 17:00 

# 我后来想了一下，确实不能用 while cnt == k: 这种写法，因为这个不会回头统计左边的或直接加上右边的。 

# 2026.02.04 17:03 