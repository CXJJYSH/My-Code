from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        
        for i, x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            
            if i - q[0] + 1 > k:
                q.popleft()
            
            if i >= k - 1:
                ans.append(nums[q[0]])
        
        return ans 