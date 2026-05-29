class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s) 

        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                if ord(s[left]) < ord(s[right]):
                    s[right] = s[left]
                    left += 1
                    right -= 1
                else:
                    s[left] = s[right]
                    left += 1
                    right -= 1
            else:
                left += 1
                right -= 1
        
        return "".join(s) 
    
# 三分钟完成这道题，简单题。 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.03.13 12:59 

# 灵神把相等的情况合并到前面大于后面的情况了，这样完全没问题，丝毫不影响。 
# 还发现字典序可以直接比较。 

# 灵神说这是贪心算法，但是怎么灵神的这段代码速度比我用相向双指针写的还慢一些啊。 

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s) 

        for i in range(len(s)):
            x = s[i]
            y = s[-1 - i]
        
            if x > y:
                s[i] = y
            else:
                s[-1 - i] = x
        
        return "".join(s) 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.03.12 13:07 