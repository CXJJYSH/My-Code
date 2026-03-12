class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s) 
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] in "aeiouAEIOU" and s[right] in "aeiouAEIOU":
                s[left], s[right] = s[right], s[left] 
                left += 1
                right -= 1
        
            while not s[left] in "aeiouAEIOU" and left < right:
                left += 1
            while not s[right] in "aeiouAEIOU" and left < right:
                right -= 1
        
        return "".join(s) 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.03.12 22:14 

# 我的另一份写法，这一份逻辑结构更简单。 

class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s) 

        left = 0
        right = len(s) - 1

        while left < right:
            while not s[left] in "aeiouAEIOU" and left < right:
                left += 1
            while not s[right] in "aeiouAEIOU" and left < right:
                right -= 1

            s[left], s[right] = s[right], s[left] 
            left += 1
            right -= 1

        return "".join(s) 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.03.12 23:07 

# 这道题也没看到灵神的题解，直接过了。 

# 2026.03.12 23:12 