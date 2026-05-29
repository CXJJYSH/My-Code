# 自己写的代码 

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        first_word = list(words[0])
        num = 0
        for c in first_word:
            if c in "aeiou":
                num += 1
        for i in range(1, len(words)):
            word = list(words[i])
            cur_num = 0
            for c in word:
                if c in "aeiou":
                    cur_num += 1
            if cur_num == num:
                left = 0
                right = len(word) - 1
                while left < right:
                    word[left], word[right] = word[right], word[left]
                    left += 1
                    right -= 1
            words[i] = "".join(word)
        return " ".join(words)

# 时间复杂度O(n)，因为最多不超过2 * n次操作。 
# 空间复杂度O(n) 

# 2026.02.18 18:00 

# 2026.02.19 22:03 

# 2026.02.20 23:30 

# 2026.02.21 23:40 

# 2026.02.22 22:26 

# 2026.02.23 22:02 正月初七 

# 2026.02.24 11:00 

# 2026.02.25 19:53 

# 2026.02.26 23:37 

# 2026.02.27 21:34 

# 2026.02.28 21:41 

# 2026.03.01 20:39 

# 2026.03.02 08:28 

# 2026.03.03 22:35 

# 2026.03.04 22:21 

# 2026.03.05 22:48 

# 2026.03.06 23:28 明天开始学技术。 

# 2026.03.07 23:03 诶，卧槽，TMD感冒了。 换了个新梯子，Kitty Network，看看怎么样。 可以用，再看看稳定性。 稳定性也很不错。 可以用GPT油管Github和Steam，和其它墙内网站也不冲突，目前感觉非常好用。 就是用不了Gemini，当然这个用啥梯子也用不了。 

# 2026.03.08 23:29 今天打了会儿星际战甲，没看。 为什么今天用Kitty又没效果了。 换回小火箭才有用。 过了一会儿Kitty又好了。 

# 2026.03.09 14:24 今天看下Kitty行不行。 OK，可以。 

# 2026.03.10 23:07 今天周二，好多课，只有早八没课，快燃尽了。先不搞了。 

# 2026.03.11 23:06 回归 时隔20天 

# 灵神的写法 

# 在类之外创建了一个函数。 

def count_vowel(s: str) -> int:
    return sum(c in "aeiou" for c in s)

class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        cnt0 = count_vowel(a[0])

        for i in range(1, len(a)):
            if count_vowel(a[i]) == cnt0:
                a[i] = a[i][::-1]
        
        return " ".join(a)
        
# 思路和我是完全一样的，但是灵神计算元音个数封装成了一个函数，反转时直接调用了库函数，比我的更简洁。 
# 但是时空复杂度是一样的。 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.03.11 23:10 