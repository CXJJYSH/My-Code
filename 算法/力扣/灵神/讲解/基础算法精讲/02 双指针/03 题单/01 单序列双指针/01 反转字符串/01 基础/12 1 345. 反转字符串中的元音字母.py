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