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
# 空间复杂度O(U)（哈希集合写法）。 
# 如果是数组写法，空间复杂度O(|Σ|)，|Σ|为本题中创建的数组的大小，本题中|Σ|比U大。 

# 2026.01.22 23:29 

# 优化写法 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = defaultdict(int) # 哈希表写法。 
        for c in t:
            cnt[c] += 1
        less = len(cnt)

        ans_left, ans_right = -1, len(s)
        left = 0

        for right, c in enumerate(s):
            cnt[c] -= 1
            if cnt[c] == 0:
                less -= 1
            # 这里用less表示滑动窗口中个数少于t中的字符个数。 

            while less == 0: # 优化写法这里不用进行两个集合的大小比较，少了O(U)的时间复杂度，所以时间复杂度更小了。 
                if right - left < ans_right - ans_left:
                    ans_left, ans_right = left, right 
                # 更新答案。 

                out = s[left]
                if cnt[out] == 0:
                    less += 1
                # 处理边界条件。 

                cnt[out] += 1
                left += 1
                # 正常更新。 

        return "" if ans_left < 0 else s[ans_left : ans_right + 1] 
        # 条件判断返回值。 

# 时间复杂度O(m + n)（哈希表写法）。 
# 如果是数组写法，创建了大小为|Σ|的数组，那么时间复杂度为O(m + n +|Σ|)。 

# 空间复杂度O(n)（哈希表写法）。 
# 空间复杂度O(|Σ|)（数组写法）。 

# 2026.01.22 23:53 