class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                while s[left] == s[left + 1] and left < right - 1:
                    left += 1
                while s[right] == s[right - 1] and left < right - 1:
                    right -= 1
                left += 1
                right -= 1
            else:
                return right - left + 1
        return right - left + 1
    
# 我自己写的代码。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.03.14 22:58 

# 力扣官方的写法。没看到灵神的题解。 

class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            c = s[left]
        
            while left <= right and s[left] == c: # left < right 放到前面竟然可以防越界。 
                left += 1
            while left <= right and s[right] == c: # left < right 放到前面竟然可以防越界。 
                right -= 1

        return right - left + 1
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.03.14 23:20 

# 我又对我自己的代码进行了改编。 

class Solution:
    def minimumLength(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while left < right and s[left] == s[right]:
            while s[left] == s[left + 1] and left < right - 1:
                left += 1
            while s[right] == s[right - 1] and left < right - 1:
                right -= 1
        
            left += 1
            right -= 1
        
        return right - left + 1

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.03.14 23:26 