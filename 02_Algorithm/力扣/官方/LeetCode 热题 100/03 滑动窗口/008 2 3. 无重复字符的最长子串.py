from collections import defaultdict
from typing import Counter

# 2025.10.19 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 时间复杂度 O(n)
        # 空间复杂度 O(128) O(1) O(len(set(s)))
        ans = 0
        cnt = Counter() # 建立一个hashmap，键是字符，值是出现次数。
        left = 0
        for right, x in enumerate(s):
            cnt[x] += 1
            while cnt[x] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
    
# 2026.06.10 11:43 

# 哈希表（整型数组） 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        cnt = defaultdict(int) 
        
        left = 0
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans 
    
# 哈希集合（布尔数组） 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        window = set()

        left = 0
        for right, c in enumerate(s):
            while c in window:
                window.remove(s[left])
                left += 1
            window.add(c)
            ans = max(ans, right - left + 1)

        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(U)，U为字符集合的大小。  

# 2026.06.10 12:02 