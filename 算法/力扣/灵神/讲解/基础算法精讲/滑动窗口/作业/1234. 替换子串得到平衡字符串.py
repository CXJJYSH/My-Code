from collections import Counter
from math import inf

class Solution:
    def balancedString(self, s: str) -> int:

        # 看完题解之后自己写一遍就通过了，真爽。
        
        m = len(s) // 4
        cnt = Counter(s)
        if len(cnt) == 4 and min(cnt.values()) == m:
            return 0
        ans = inf
        left = 0
        for right, i in enumerate(s):
            cnt[i] -= 1
            while max(cnt.values()) <= m:
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1
                left += 1
        return ans
    
# 算术评级7的中等题，用时23分钟。
# 2025.10.30 21:14