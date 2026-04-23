from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        
        # 定长滑窗优化写法，与76.最小覆盖子串的优化方法一样，都是用一个less变量来维护是否达标的状态。

        cnt = defaultdict(int)
        for c in p:
            cnt[c] += 1
        ans = []
        less = len(cnt)
        left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1
            if cnt[c] == 0:
                less -= 1
            while right - left + 1 > len(p):
                x = s[left]
                if cnt[x] == 0:
                    less += 1
                cnt[x] += 1
                left += 1
            if less == 0:
                ans.append(left)
        return ans

        # 定长滑窗
        '''
        ans = []
        cnt_p = Counter(p)
        cnt_s = Counter()
        for right, c in enumerate(s):
            cnt_s[c] += 1
            left = right - len(p) + 1
            if left < 0:
                continue
            if cnt_s == cnt_p:
                ans.append(left)
            cnt_s[s[left]] -= 1
            if cnt_s[s[left]] == 0:
                del cnt_s[s[left]]
        return ans
        '''
        # 不定长滑窗
        
        '''
        ans = []
        cnt = Counter(p)
        left = 0
        for right, x in enumerate(s):
            cnt[x] -= 1
            while cnt[x] < 0:
                cnt[s[left]] += 1
                left += 1
            if right - left + 1 == len(p):
                ans.append(left)
        return ans
        '''
        # 2025.10.20 23:58 

#2025.10.21 15:52