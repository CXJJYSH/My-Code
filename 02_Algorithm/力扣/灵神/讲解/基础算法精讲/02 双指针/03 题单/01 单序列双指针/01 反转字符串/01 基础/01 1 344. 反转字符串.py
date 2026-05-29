from typing import List

# 双指针写法 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        left = 0
        right = len(s) - 1

        while left < right: 
            s[left], s[right] = s[right], s[left] 

            left += 1
            right -= 1
        
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.02.07 14:13 

# 单指针写法 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for i in range(len(s) // 2):
            s[i], s[- i - 1] = s[- i - 1], s[i] 
            
# 循环到i等于len(s) // 2（向下取整）的时候停止， 
# 因为当 n = len(s) 是偶数的时候，i等于n // 2的时候刚好超过了左中那个元素， 
# 当 n = len(s) 是奇数时，i等于n // 2时刚好在正中间的元素，此时不用交换。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.02.07 14:23 

# 库函数写法 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        s.reverse() 

# 有些语言可以直接调用库函数完成这道题。 

# Python中这种写法是最快的。
# 双指针第二快。 
# 单指针最慢。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.02.07 14:26 