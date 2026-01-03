from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        
        for right, c in enumerate(s):
            cnt[c] += 1
            
            while cnt[c] > 2:
                cnt[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans 

# 时间复杂度O(n + U)，n为s长度，U为s中不同字符的个数。 
# 空间复杂度O(U)，U为s中不同字符的个数。 

# 2026.01.03 17:48 