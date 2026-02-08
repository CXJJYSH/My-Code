class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        place = 0
        for right, x in enumerate(word):
            if x == ch:
                place = right 
                break
        
        s = list(word) 
        left = 0
        right = place 
        
        while left < right: 
            s[left], s[right] = s[right], s[left] 
            left += 1
            right -= 1
        
        return "".join(s) 
    
# 一遍过 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.02.08 11:43 

# 下面的写法应该更快一点，因为在第一个for循环里面就可以直接判断索引是否为最后一个然后返回字符串。 

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        place = 0
        for right, x in enumerate(word):
            if x == ch:
                place = right
                if place == -1:
                    return word  
                break
        
        word = list(word) 
        left = 0
        right = place 
        
        while left < right: 
            word[left], word[right] = word[right], word[left] 
            left += 1
            right -= 1
        
        return "".join(word) 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.02.08 11:55 