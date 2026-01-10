from heapq import heapify, heapreplace
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h = [(arr[0], i, 0) for i, arr in enumerate(nums)]
        heapify(h)

        ans_l = h[0][0]
        ans_r = max(arr[0] for arr in nums)
        r = max(arr[0] for arr in nums)
        
        while h[0][2] < len(nums[h[0][1]]) - 1: # while语句条件的含义：https://chatgpt.com/c/696273cb-74c0-832e-a2ab-f34ade66d5ea 
            _, i, j = h[0] 
            
            x = nums[i][j + 1]
            heapreplace(h, (x, i, j + 1))
            
            r = max(r, x)
            l = h[0][0]
            
            if r - l < ans_r - ans_l:
                ans_l, ans_r = l, r 
        
        return [ans_l, ans_r] 
    
# 这个堆的方式第一次见，还真挺难理解的，多看灵神的解析和GPT的讲解加深理解才好。 

# 时间复杂度O(L log n) 
# 空间复杂度O(n) 

# 2026.01.10 23:57 