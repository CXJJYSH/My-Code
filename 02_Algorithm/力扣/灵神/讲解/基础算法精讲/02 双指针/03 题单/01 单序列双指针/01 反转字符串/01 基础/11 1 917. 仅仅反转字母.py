class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s) 
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left].isalpha() and s[right].isalpha():
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
            while not s[left].isalpha() and left < right:
                left += 1
        
            while not s[right].isalpha() and left < right:
                right -= 1
        
        return "".join(s) 
    
# 回归之后的第一道新题，简单题，秒杀，时间复杂度超越100%。 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.03.11 23:27 

# 没看到灵神的题解，直接过吧。 

# 2026.03.11 23:28 