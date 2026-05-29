from itertools import count

# 递归写法 

class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return s 

        if s[0].isalpha():
            return s[0] + self.decodeString(s[1:]) 

        i = s.find('[') 
        balance = 1
        for j in count(i + 1):
            if s[j] == '[':
                balance += 1
            elif s[j] == ']':
                balance -= 1
                if balance == 0:
                    return self.decodeString(s[i + 1 : j]) * int(s[:i]) + self.decodeString(s[j + 1:])
                
# 栈写法 

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        res = ''
        k = 0
        
        for c in s:
            if c.isalpha():
                res += c 
            elif c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                stack.append((res, k))
                res = ''
                k = 0
            else:
                pre_res, pre_k = stack.pop()
                res = pre_res + res * pre_k 
        
        return res 
    
# 可以通过画图理解。 

# 时间复杂度O(U ** m) 
# 空间复杂度O(U ** m) 

# 2026.05.19 11:59 