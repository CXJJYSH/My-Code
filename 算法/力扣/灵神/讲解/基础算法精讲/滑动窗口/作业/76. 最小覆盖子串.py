from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # 如下是复刻的灵神的题解。
        
        # 一般写法
        
        '''
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
        '''
        
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
    
# 没想到这道题之前就已经做过了，2025.10.21做的，今天是2025.10.31，又跳到了这道题，光看题目竟然没想起来这道题之前就已经做过了。
# 困难题 2025.10.31 11:11 
# 至此灵神基础算法精讲滑动窗口的作业题就全部做完了，该开启下一阶段了。 