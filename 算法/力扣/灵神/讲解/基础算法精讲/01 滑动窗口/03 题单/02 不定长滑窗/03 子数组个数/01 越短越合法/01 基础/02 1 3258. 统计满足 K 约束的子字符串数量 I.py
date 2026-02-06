# 我的写法————条件判断。 

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        cnt0 = 0 
        cnt1 = 0
        left = 0

        for right, x in enumerate(s):
            if x == '0':
                cnt0 += 1
            else:
                cnt1 += 1
            
            while cnt0 > k and cnt1 > k:
                if s[left] == '0':
                    cnt0 -= 1
                else:
                    cnt1 -= 1
                left += 1
            
            ans += right - left + 1
        
        return ans 
    
# 思路完全没问题，最大的问题是0和1是字符，不是数字，所以条件判断的时候不能和数字进行比较。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.24 23:58 

# 灵神的写法————ASCII码与1（&1）快速取末位。 

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        cnt = [0, 0]
        left = 0

        for right, x in enumerate(s):
            cnt[ord(x) & 1] += 1
            
            while cnt[0] > k and cnt[1] > k:
                cnt[ord(s[left]) & 1] -= 1
                left += 1
            
            ans += right - left + 1
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.25 00:07 

# 也可以模2（%2）快速取末位。 

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        ans = 0
        cnt = [0, 0]
        left = 0

        for right, x in enumerate(s):
            cnt[ord(x) % 2] += 1
            
            while cnt[0] > k and cnt[1] > k:
                cnt[ord(s[left]) % 2] -= 1
                left += 1
            
            ans += right - left + 1
        
        return ans 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.25 00:11 