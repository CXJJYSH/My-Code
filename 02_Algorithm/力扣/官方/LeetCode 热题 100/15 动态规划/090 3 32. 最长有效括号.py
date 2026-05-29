class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s) 
        is_valid = [False] * n 
        st = []

        for i, ch in enumerate(s):
            if ch == '(':
                st.append(i)
            elif st:
                is_valid[i] = is_valid[st.pop()] = True 

        ans = cnt = 0
        for b in is_valid:
            if b:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 0
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.05.29 12:05 

# 优化先懒得管 
# https://leetcode.cn/problems/longest-valid-parentheses/?envType=study-plan-v2&envId=top-100-liked 

# 2026.05.29 12:05 