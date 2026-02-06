from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        
        s = 0
        
        for i, x in enumerate(arr):
            s += x
            
            left = i - k + 1
            
            if i < k - 1:
                continue
            
            if s / k >= threshold:
                ans += 1
            
            s -= arr[left]
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.01 15:29 