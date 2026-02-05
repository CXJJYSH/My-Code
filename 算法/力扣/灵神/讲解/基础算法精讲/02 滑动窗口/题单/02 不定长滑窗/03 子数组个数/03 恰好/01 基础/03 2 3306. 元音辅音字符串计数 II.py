# 3306. 元音辅音字符串计数 II

# 给你一个字符串 word 和一个 非负 整数 k。

# 返回 word 的 子字符串 中，每个元音字母（'a'、'e'、'i'、'o'、'u'）至少 出现一次，并且 恰好 包含 k 个辅音字母的子字符串的总数。

from collections import defaultdict

# 我自己写的一段代码，有问题，测试的时候第三个例子就没通过。 
# 但是问了两次GPT之后还是不知道问题在哪里。 

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def solve(k):
            ans = 0
            cnt1 = defaultdict(int) 
            cnt2 = defaultdict(int) 
            left = 0

            for x in word:
                if x in "aeiou":
                    cnt1[x] += 1
                else:
                    cnt2[x] += 1
            
                while len(cnt1) == 5 and len(cnt2) >= k:
                    out = word[left] 
            
                    if out in "aeiou":
                        cnt1[out] -= 1
                        if cnt1[out] == 0:
                            del cnt1[out]
                    else:
                        cnt2[out] -= 1
                        if cnt2[out] == 0:  
                            del cnt2[out] 
            
                    left += 1
            
                ans += left 
            
            return ans 
        
        return solve(k) - solve(k + 1) 
    
# 看完灵神的题解知道问题出在哪了，题目要求是至少 5 “种” 元音、和至少 k “个” 辅音，这里的辅音不是统计种类，而是各个种类的辅音数量加起来。 
# 所以元音的统计需要用到字典，而辅音的统计只需要用到一个额外变量统计总个数就可以了。
# 之后改了一遍就通过了。 

# 我一开始的思路是没错的，是题目意思搞错了。 

# 通过的最基础版。 

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def solve(k):
            ans = 0
            cnt1 = defaultdict(int) 
            cnt2 = 0
            left = 0

            for x in word:
                if x in "aeiou":
                    cnt1[x] += 1
                else:
                    cnt2 += 1

                while len(cnt1) == 5 and cnt2 >= k:
                    out = word[left] 

                    if out in "aeiou":
                        cnt1[out] -= 1
                        if cnt1[out] == 0:
                            del cnt1[out]
                    else:
                        cnt2 -= 1

                    left += 1

                ans += left 

            return ans 

        return solve(k) - solve(k + 1) 
    
# 时间复杂度O(n) 
# 空间复杂度O(1)，字典的大小是确定的，就O(5)的大小。 

# 2026.02.05 17:07 

# 这是灵神用了两个函数的基础版。

class Solution:
    def f(self, word: str, k: int) -> int:
        cnt1 = defaultdict(int) 
        ans = cnt2 = left = 0 

        for b in word:
            if b in "aeiou":
                cnt1[b] += 1
            else:
                cnt2 += 1
        
            while len(cnt1) == 5 and cnt2 >= k:
                out = word[left]
        
                if out in "aeiou":
                    cnt1[out] -= 1
                    if cnt1[out] == 0:
                        del cnt1[out]
                else:
                    cnt2 -= 1
                left += 1
        
            ans += left
        
        return ans

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.f(word, k) - self.f(word, k + 1)
    
# 这个版本的函数调用的时候要传入两个参数。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2025.02.05 17:11 

# 优化一：位运算 
# 灵神说Python代码无需优化。 

class Solution:
    def f(self, word: str, k: int) -> int:
        cnt1 = defaultdict(int) 
        ans = cnt2 = left = 0 

        for b in word:
            if b in "aeiou":
                cnt1[b] += 1
            else:
                cnt2 += 1
        
            while len(cnt1) == 5 and cnt2 >= k:
                out = word[left]
        
                if out in "aeiou":
                    cnt1[out] -= 1
                    if cnt1[out] == 0:
                        del cnt1[out]
                else:
                    cnt2 -= 1
                left += 1
        
            ans += left
        
        return ans

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.f(word, k) - self.f(word, k + 1) 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.02.05 17:12 

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        ans = 0 
        
        cnt_vowel1 = defaultdict(int) 
        cnt_vowel2 = defaultdict(int) 
        
        cnt_consonant1 = 0
        cnt_consonant2 = 0
        
        left1 = 0
        left2 = 0
        
        for x in word:
            if x in "aeiou":
                cnt_vowel1[x] += 1
                cnt_vowel2[x] += 1
            else:
                cnt_consonant1 += 1
                cnt_consonant2 += 1
        
            while len(cnt_vowel1) == 5 and cnt_consonant1 >= k:
                # 统计辅音个数大于等于k的子字符串数量。 

                out = word[left1] 
        
                if out in "aeiou":
                    cnt_vowel1[out] -= 1
                    if cnt_vowel1[out] == 0:
                        del cnt_vowel1[out] 
                else:
                    cnt_consonant1 -= 1
        
                left1 += 1
                # 这个循环统计的是 0 到 left1 - 1 的子字符串起点数量。 
                # 共left1个。 

            while len(cnt_vowel2) == 5 and cnt_consonant2 >= k + 1:
                # 统计辅音个数大于等于k + 1的子字符串数量。 

                out = word[left2] 
        
                if out in "aeiou":
                    cnt_vowel2[out] -= 1
                    if cnt_vowel2[out] == 0:
                        del cnt_vowel2[out] 
                else:
                    cnt_consonant2 -= 1
        
                left2 += 1
                # 这个循环统计的是 0 到 left2 - 1 的子字符串起点数量。 
                # 共left2个。 

            ans += left1 - left2 
            # 寻常的双指针窗口是每个右端点统计对应的子字符串数量，然后对and进行加算。 
            # 而这里是三指针窗口，对于每个右端点来说，符合条件的子字符串数量 在两个左端点之间， 
            # 两个左端点停止时，都是停在刚好不符合while循环条件的位置， 
            # 所以两个左端点前一个元素刚好就是符合循环条件的所有起点的终点位置， 
            # 而范围分别时从 0 到 left1 - 1 ，和 从 0 到 left2 - 1 ， 
            # 分别时left1个和left2个起点， 
            # 而根据算法原理要用两个总数相减，就能算出辅音个数刚好为k的子字符串个数， 
            # 而这个子字符串个数只是针对当前右端点来说的， 
            # 所以每一次for循环的最后要对ans进行加算，不断累计符合条件的子字符串个数，for循环结束时ans刚好就是正确的答案数量。 

        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 灵神说空间复杂度还能说是O(U)，U为21。 
# 我觉得U为5吧，或者为 5 + 5 == 10 。 
# 怎么也不会是21吧，这里统计元音用到了字典，统计辅音没用到字典。 

# 2026.02.05 17:37 