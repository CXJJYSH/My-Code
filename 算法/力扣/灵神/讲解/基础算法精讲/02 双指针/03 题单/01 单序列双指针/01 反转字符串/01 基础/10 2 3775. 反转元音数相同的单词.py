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

# 2026.03.07 23:03 诶，卧槽，TMD感冒了。 换了个新梯子，Kitty Network，看看怎么样。 可以用，再看看稳定性。 稳定性也很不错。 可以用GPT油管和Github，和其它墙内网站也不冲突，目前感觉非常好用。 