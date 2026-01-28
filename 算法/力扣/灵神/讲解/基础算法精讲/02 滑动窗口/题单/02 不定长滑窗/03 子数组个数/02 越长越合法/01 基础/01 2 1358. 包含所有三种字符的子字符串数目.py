from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        cnt = defaultdict(int)
        left = 0
        
        for c in s:
            cnt[c] += 1
            
            while len(cnt) == 3:
                out = s[left] 
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
                left += 1
            
            ans += left 
        
        return ans 
    
# 越长越合法型就是将循环条件写成符合条件的语句，跳出循环的时候刚好就是不符合条件的情况， 
# 说明上一个情况以及之前的情况都是符合条件的情况， 
# 然后根据数量关系计算符合条件的情况个数即可。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 用时10:40。 

# 2026.01.28 17:52 