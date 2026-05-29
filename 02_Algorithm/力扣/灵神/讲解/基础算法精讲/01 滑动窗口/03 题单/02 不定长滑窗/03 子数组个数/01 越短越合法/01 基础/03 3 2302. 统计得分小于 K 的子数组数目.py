from typing import List

# 困难题 

# 之前第一遍做的时候写的代码。
# 2025.10.28 

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        # 我自己想到的基础滑窗实现是没问题的，在个数计算的时候有问题。
        # 没有和昨天的“越长越合法”类型的题目联系起来，没有看出这是“越短越合法”类型的题目，所以少了计算答案个数的细节。
        # 而且看了题解之后意识到了这是“越短越合法”类型的题目之后，个数计算还没有考虑周全，少了最小单位的情况。最后运行错误看完了题解代码之后才意识过来。
        # 虽然这道题用时00:25:05较短，但是仍应该郑重重视。

        ans = 0
        left = 0
        sum = 0
        for right, i in enumerate(nums):
            sum += i 
            while sum * (right - left + 1) >= k:
                sum -= nums[left]
                left += 1
            ans += (right - left + 1)
        return ans
    
# 第二次做的时候我自己写的代码。 
# 2026.01.25 11:14 

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0 
        s = 0
        left = 0

        for right, x in enumerate(nums):
            s += x 
            score = s * (right - left + 1)
            
            while score >= k:
                s -= nums[left] 
                left += 1
                score = s * (right - left + 1)
            
            ans += right - left + 1
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.25 11:15 

# 第二遍写完之后又看灵神的题解改进了的代码。 

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        s = 0
        left = 0

        for right, x in enumerate(nums):
            s += x 
            
            while s * (right - left + 1) >= k:
                s -= nums[left] 
                left += 1
            
            ans += right - left + 1
        
        return ans 
    
# 这个优化的地方在于没有再用一个变量表示子数组的分数了，之后用表达式表示出来在循环条件里。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.25 11:20 

# 感觉这是近期遇到的最简单的一道困难题。 

# 2026.01.25 11:21 