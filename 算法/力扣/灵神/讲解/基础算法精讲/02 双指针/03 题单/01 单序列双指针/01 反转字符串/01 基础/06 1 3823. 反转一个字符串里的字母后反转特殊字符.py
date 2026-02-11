from typing import Callable, List

# 我的代码 

class Solution:
    def reverseByType(self, s: str) -> str:
        s = list(s) 
        n = len(s) 
        
        left = 0
        right = n - 1
        while left <= right:
            if s[left].islower() and s[right].islower():
                s[left], s[right] = s[right], s[left] 
                left += 1
                right -= 1
        
            while left < n and not s[left].islower():
                left += 1
            while right >= 0 and not s[right].islower():
                right -= 1
        
        left = 0
        right = n - 1
        while left <= right:
            if not s[left].islower() and not s[right].islower():
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1 
        
            while left < n and s[left].islower():
                left += 1
            while right >= 0 and s[right].islower():
                right -= 1
        
        return "".join(s) 
    
# 时间复杂度O(n) 
# 空间复杂度O(n)，s = list(s)占用O(n)额外空间。 

# 2026.02.11 15:16 

# 灵神的代码 

class Solution:
    def reverse(self, t: List[str], f: Callable[[str], bool]) -> None:
        left = 0
        right = len(t) - 1
        while left < right:
            while left < right and f(t[left]):
                left += 1
            while left < right and f(t[right]):
                right -= 1
            t[left], t[right] = t[right], t[left]
            left += 1
            right -= 1

    def reverseByType(self, s: str) -> str:
        t = list(s) 
        self.reverse(t, str.islower) 
        self.reverse(t, lambda ch: not ch.islower())
        return "".join(t) 

# 时间复杂度O(n) 
# 空间复杂度O(n)，Python不能原地修改字符串。 

# 2026.02.11 16:05 