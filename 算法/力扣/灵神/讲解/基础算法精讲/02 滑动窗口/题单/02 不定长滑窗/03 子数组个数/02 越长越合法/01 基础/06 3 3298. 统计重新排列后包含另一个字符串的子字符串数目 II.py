from collections import defaultdict

# 看了灵神的题解说和76题很像就去看了一下76题的代码，之后顺利自己写出了这道题应该用的代码，并符合题目要求的时间复杂度。 

# 和灵神的题解几乎一模一样，只是少了一个剪枝（边界条件判断）。 

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        ans = 0

        cnt = defaultdict(int)
        for c in word2:
            cnt[c] += 1

        less = len(cnt)

        left = 0

        for x in word1:
            cnt[x] -= 1
            if cnt[x] == 0:
                less -= 1

            while less == 0:
                out = word1[left]

                if cnt[out] == 0:
                    less += 1

                cnt[out] += 1

                left += 1

            ans += left

        return ans 
    
# 时间复杂度O(n + U)，U是字符集合的大小，最开始统计word2中各字符的个数用了U的时间复杂度。 
# 空间复杂度O(U)，U是字符集合的大小。 

# 2026.02.02 11:17 

# 2026.02.02 11:21 

# 完完全全和灵神一样了。 

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            return 0
        
        ans = 0
        
        diff = defaultdict(int) 
        for x in word2:
            diff[x] += 1
        
        less = len(diff) 
        
        left = 0
        
        for x in word1:
            diff[x] -= 1
            if diff[x] == 0:
                less -= 1
        
            while less == 0:
                out = word1[left] 
        
                if diff[out] == 0:
                    less += 1
                diff[out] += 1
        
                left += 1
        
            ans += left 
        
        return ans 
    
# 时间复杂度O(n + U)，U为字符集合大小。 
# 空间复杂度O(U)，U为字符集合大小。 

# 2026.02.02 11:27 

# 是否有边界条件判断剪枝会导致代码有些许复杂度差异，可以在本题的提交记录里查看。 

# 2026.02.02 11:30 