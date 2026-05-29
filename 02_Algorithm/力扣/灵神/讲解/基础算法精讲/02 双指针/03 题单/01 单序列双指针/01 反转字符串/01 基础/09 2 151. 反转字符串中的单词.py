# 自己写出来的 

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s[::-1]
        s = s.split() # 结果为元素为字符串的列表。 

        for i in range(len(s)):
            word = list(s[i]) # 不能直接对字符串进行索引操作，所以要先将字符串转换为单字符组成的列表。 
        
            left = 0
            right = len(s[i]) - 1
            while left < right:
                word[left], word[right] = word[right], word[left] 
                left += 1
                right -= 1
        
            s[i] = "".join(word) # 最后再将反转后的列表中的元素合并形成新的字符串代替之前的字符串。 

        return " ".join(word for word in s) # 最后再将分开的字符串合并成最长的字符串。 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.02.17 17:15 