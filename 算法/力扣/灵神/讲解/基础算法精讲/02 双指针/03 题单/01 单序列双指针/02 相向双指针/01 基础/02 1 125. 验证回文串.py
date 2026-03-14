class Solution:
    def isPalindrome(self, s: str) -> bool:
        #第一段是我自己写的代码，解答错误了。后来去问了GPT，修改了一点，但标点没有考虑，所以仍然解答错误。
        
        '''    
        s = s.replace(" ", "")
        s = s.lower()
        s = list(s)
        n = len(s)
        pre = []
        suf = []
        for i in range(n):
            pre.append(s[i])
        for j in range(n - 1, -1, -1):
            suf.append(s[j])
        for a, b in zip(pre, suf):
            if a != b:
                return False
        return True
        '''
        
        #第二段是依照灵神的题解来写的，灵神说“简单题，简单做”，这样写确实是简单又优雅。
        
        '''
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True
        '''
        
        #第三段是GPT提供的最简代码。

        # 2026.03.14 22:18 又复刻了一遍GPT的写法。 
        
        s = "".join(a.lower() for a in s if a.isalnum())
        return s == s[::-1]
    
        # 2026.03.14 22:23 又写了一遍灵神的代码。 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            
            # 先排除非字母数字字符的情况。 

            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
        
            # 然后如果前后一直都相等就一直同步移动指针，注意要调成小写形式。 

            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            
            # 一旦出现了不等的就返回False。 

            else:
                return False
        
        # 如果一直没有出现不等的，即一直相等，则返回True。 

        return True
    
# 灵神 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# GPT 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.03.14 22:28 