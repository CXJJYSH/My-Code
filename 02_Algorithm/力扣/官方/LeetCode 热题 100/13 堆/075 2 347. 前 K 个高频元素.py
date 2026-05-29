from typing import Counter, List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums) 
        max_cnt = max(cnt.values())

        buckets = [[] for _ in range(max_cnt + 1)] 
        for key, val in cnt.items():
            buckets[val].append(key) 

        ans = []
        for bucket in reversed(buckets):
            ans += bucket 
            if len(ans) == k:
                return ans 
            
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.05.21 22:09 