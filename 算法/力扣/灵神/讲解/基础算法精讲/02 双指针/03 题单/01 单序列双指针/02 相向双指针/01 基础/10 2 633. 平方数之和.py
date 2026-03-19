from math import isqrt

# 判断一个数是否能由两个平方数组成。 

# 灵神的枚举方法。 

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0

        while a * a * 2 <= c:
            b = isqrt(c - a * a) 
            if a * a + b * b == c:
                return True
            a += 1
        
        return False 
    
# 时间复杂度O(根号c)，开平方有专门的CPU指令，可以视作O(1)。 
# 空间复杂度O(1) 

# 2026.03.19 10:59 

# 灵神的相向双指针写法 

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, isqrt(c) 

        while a <= b:
            s = a * a + b * b 
        
            if s == c:
                return True
            elif s < c:
                a += 1
            else:
                b -= 1
        
        return False 
    
# 我没想出相向双指针的写法关键在于我没想到可以直接用isqrt(c)确定左右指针的右边界，然后左右指针从两边向中间靠拢来寻找符合条件的答案。 
    
# 时间复杂度O(根号c) 
# 空间复杂度O(1) 

# 2026.03.19 11:08 