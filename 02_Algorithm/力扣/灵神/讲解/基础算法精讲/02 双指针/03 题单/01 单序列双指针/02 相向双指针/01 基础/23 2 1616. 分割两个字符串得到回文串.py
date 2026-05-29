# 2026.04.04 23:44 

# 2026.04.05 23:53 

# 我自己写的两版代码，都超出时间限制了。 

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        for i in range(len(a)):
            a_pre = a[0 : i + 1]
            a_suf = a[i + 1:]
            b_pre = b[0 : i + 1]
            b_suf = b[i + 1:]
            af = a_pre + b_suf 
            bf = b_pre + a_suf 
            if af == af[::-1] or bf == bf[::-1]:
                return True 
        return False 
    
class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        for i in range(len(a) + 1):
            a_pre = a[0 : i]
            a_suf = a[i:]
            b_pre = b[0 : i]
            b_suf = b[i:]
            af = a_pre + b_suf 
            bf = b_pre + a_suf 
            if af == af[::-1] or bf == bf[::-1]:
                return True 
        return False 

# 灵神的写法 

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(a: str, b: str):
            i = 0
            j = len(a) - 1
            while i < j and a[i] == b[j]:
                i += 1
                j -= 1
            s = a[i : j + 1]
            t = b[i : j + 1]
            return s == s[::-1] or t == t[::-1]
        return check(a, b) or check(b, a)

# check函数的两个参数分别代表前缀和后缀 
# 两头匹配若干字符后，去判断中间部分是否有回文串 
# 因为无非是a加上中间段当前缀或者b加上中间段当后缀 
# 但是check函数里固定了第一个参数占了前缀，第二个参数占了后缀 
# 所以最后return时要返回传入两次参数分别做前后缀的or结果。 

# 时间复杂度O(n)，各部分时间复杂度加起来最多就是n。 
# 空间复杂度O(1) 

# 2026.04.06 23:51 