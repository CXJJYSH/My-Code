from collections import Counter, defaultdict

# 2025.10.21 

# 2025.01.11 

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
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right 
                out = s[left]
                if cnt[out] == 0:
                    less += 1
                cnt[out] += 1
                left += 1
        return "" if ans_left < 0 else s[ans_left : ans_right + 1]

# 2026.04.15 12:11 

# 这是优化写法 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_left = -1
        ans_right = len(s) 

        cnt = defaultdict(int)
        for i in t: 
            cnt[i] += 1
        
        less = len(cnt)

        left = 0
        for right, x in enumerate(s):
            cnt[x] -= 1
            if cnt[x] == 0:
                less -= 1
            
            while less == 0:
                if right - left < ans_right - ans_left:
                    ans_left = left 
                    ans_right = right 
                
                out = s[left] 
                if cnt[out] == 0:
                    less += 1
                cnt[out] += 1
                left += 1
        return "" if ans_left < 0 else s[ans_left : ans_right + 1]
    
# U为题目字符种类最大数目 
# m为s长度 
# n为t长度 

# 时间复杂度O(m + n) 
# 空间复杂度O(U) 

# 2026.04.15 12:19 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt_s = Counter()
        cnt_t = Counter(t) 

        ans_left, ans_right = -1, len(s) 
        left = 0

        for right, c in enumerate(s):
            cnt_s[c] += 1
            while cnt_s >= cnt_t: # 涵盖 
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right 
                cnt_s[s[left]] -= 1
                left += 1

        return "" if ans_left < 0 else s[ans_left : ans_right + 1] 
    
# 时间复杂度O(U * s + t) 
# 空间复杂度O(U) 

# 懒得写优化了，直接过。 

# 2026.06.11 16:57 