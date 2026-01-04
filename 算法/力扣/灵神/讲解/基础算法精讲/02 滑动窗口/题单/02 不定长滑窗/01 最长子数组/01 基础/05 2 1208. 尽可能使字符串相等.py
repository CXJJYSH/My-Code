class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0
        left = 0
        cost = 0
        
        for right, x in enumerate(s):
            cost += abs(ord(s[right]) - ord(t[right]))
            
            while cost > maxCost:
                cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 这道题没找到灵神的题解，感觉其他人写的还没我写的好。 

# 2026.01.04 17:38 