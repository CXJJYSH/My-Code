from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # 时间复杂度 O(n)
        # 空间复杂度 O(128) O(1) O(len(set(s)))
        
        ans = 0
        cnt = Counter() # 建立一个hashmap，键是字符，值是对应的出现次数。
        left = 0
        for right, x in enumerate(s):
            cnt[x] += 1
            while cnt[x] > 1:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans