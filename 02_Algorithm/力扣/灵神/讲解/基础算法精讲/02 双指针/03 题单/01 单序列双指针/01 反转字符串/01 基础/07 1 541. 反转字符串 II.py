class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s) 
        n = len(s) 
        
        for i in range(0, n, 2 * k):
            left = i
        
            if i + k - 1 < n:
                right = i + k - 1 
                while left < right: 
                    s[left], s[right] = s[right], s[left] 
                    left += 1
                    right -= 1
            else:
                right = n - 1
                while left < right: 
                    s[left], s[right] = s[right], s[left] 
                    left += 1
                    right -= 1
        
        return "".join(s)
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.02.12 13:14 

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s) 
        for i in range(0, len(s), 2 * k):
            s[i : i + k] = s[i : i + k][::-1]
        return "".join(s) 
    
# 切片会创建出一个新的字符串，会占用额外空间。 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.02.12 13:59 