from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        left = 0
        cnt = defaultdict(int)
        
        for right, x in enumerate(fruits):
            cnt[x] += 1
            
            while len(cnt) > 2:
                out = fruits[left] 
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1)，字典最多保存三个键值对，所以空间复杂度相当于O(1) 

# 我写的代码和灵神题解中的代码算法一模一样，时空复杂度分析也和灵神分析的分毫不差，可以说还得是灵神教得好了。 

# 2026.01.04 17:47 