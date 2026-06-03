from collections import defaultdict
from typing import List

# 2025.09.30 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            sorted_s = "".join(sorted(s))
            d[sorted_s].append(s)
        
        return list(d.values())
    
# 2026.06.03 12:43 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) 

        for s in strs:
            sorted_s = ''.join(sorted(s))
            d[sorted_s].append(s)
        
        return list(d.values()) 
    
# 时间复杂度O(n * (m log m)) 
# 空间复杂度O(n * m) 
# for循环中排序算法的时间复杂度是O(m log m)，空间复杂度O(m) 

# 2026.06.03 12:53 