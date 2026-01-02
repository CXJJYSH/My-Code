from cmath import inf
from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        cs = sum(cardPoints)
        n = len(cardPoints)
        
        m = n - k
        if m == 0:
            return cs
        # 这里需要特判m == 0的情况，原因可能是两个 
        
        # 一个是在cardPoints里找长度为0的子数组无法实现， 
        
        # 另一个是m == 0时，后面的left = i - m + 1就等于i + 1了，导致后面out = cardPoints[left]产生越界问题。 
        # 在i为cardPoints最后一个索引时才会产生越界问题。 

        s = 0
        ans = inf
        
        for i, x in enumerate(cardPoints):
            s += x
            
            left = i - m + 1
            if left < 0:
                continue
            
            ans = min(ans, s)
            
            out = cardPoints[left]
            s -= out
        
        return cs - ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.02 19:11 