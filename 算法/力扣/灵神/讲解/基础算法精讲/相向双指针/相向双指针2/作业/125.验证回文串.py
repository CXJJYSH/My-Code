class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #第一段是我自己写的代码，解答错误了。后来去问了GPT，修改了一点，但标点没有考虑，所以仍然解答错误。
            
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
        
        #第二段是依照灵神的题解来写的，灵神说“简单题，简单做”，这样写确实是简单又优雅。
        
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
        
        #第三段是GPT提供的最简代码。
        
        s = "".join(a.lower() for a in s if a.isalnum())
        return s == s[::-1]