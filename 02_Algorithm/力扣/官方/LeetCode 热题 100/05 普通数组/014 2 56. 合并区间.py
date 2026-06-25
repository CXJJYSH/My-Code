from typing import List

# 按照左端点从小到大排序 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda p : p[0]) # lambda接受p为参数，返回p[0]。 
        ans = []
        for p in intervals: 
            if ans and p[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], p[1])
            else: 
                ans.append(p)
        return ans 
    
# 时间复杂度O(n log n)，排序。  
# 空间复杂度O(1) 

# 2026.04.16 12:35 

# 排序 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda p: p[0])

        ans = []

        for p in intervals:
            if ans and p[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], p[1])
            else:
                ans.append(p)
        
        return ans 
    
# 2026.06.25 15:14 