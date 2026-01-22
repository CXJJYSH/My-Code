from collections import defaultdict
from typing import Counter

# 一般写法 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_s = Counter()
        cnt_t = Counter(t)
        ans_left, ans_right = -1, len(s)
        left = 0

        for right, c in enumerate(s):
            cnt_s[c] += 1
            
            while cnt_s >= cnt_t:
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                cnt_s[s[left]] -= 1
                left += 1
        
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]

# 时间复杂度O(U * m + n)，U为本题中Counter()集合最大大小，m为s长度，n为t长度，循环整体时间复杂度为O(U * n)，Counter(t)的时间复杂度为O(n)。 
# 空间复杂度O(U)。 

# 2026.01.22 23:29 

# 优化写法 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = defaultdict(int)
        for c in t:
            cnt[c] += 1
        less = len(cnt)
        ans_left, ans_right = -1, len(s)
        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1
            if cnt[c] == 0:
                less -= 1
            while less == 0:
                if right -left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                x = s[left]
                if cnt[x] == 0:
                    less += 1
                cnt[x] += 1
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1] 
        # 优化写法

        cnt = defaultdict(int)
        for c in t:
            cnt[c] += 1
        less = len(cnt)
        ans_left, ans_right = -1, len(s)
        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1
            if cnt[c] == 0:
                less -= 1
            while less == 0:
                if right -left < ans_right - ans_left:
                    ans_left, ans_right = left, right
                x = s[left]
                if cnt[x] == 0:
                    less += 1
                cnt[x] += 1
                left += 1
        return "" if ans_left < 0 else s[ans_left: ans_right + 1] 