# 这道题灵神又没有写题解，这是另一个人的代码。

# 说实话，没用到双指针。 

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(word[::-1] for word in s.split(" "))
    
# 自己把上面的代码改成了双指针的写法。 

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        
        for i in range(len(words)): 
            word = list(words[i])
        
            left = 0 
            right = len(word) - 1
            while left < right: 
                word[left], word[right] = word[right], word[left]
                left += 1
                right -= 1
        
            words[i] = "".join(word)
        
        return " ".join(words)
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.02.13 20:45 

# 还有两种方法。 

# 2026.02.13 20:46 

# 今天没搞 

# 2026.02.14 23:10 