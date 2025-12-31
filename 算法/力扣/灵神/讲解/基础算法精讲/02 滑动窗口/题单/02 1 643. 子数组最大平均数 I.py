from cmath import inf
from typing import List

# 正确代码 

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_s = -inf 
        s = 0
        # 初始化额外变量 

        for i, x in enumerate(nums):
            # 第一步：将元素加入定长滑窗。 
            s += x

            # 如果滑窗长度不足题目所给长度，继续加入元素。 
            if i < k - 1:
                continue

            # 第二步：更新答案 
            max_s = max(max_s, s)

            # 第三步：将不符合题意的元素删除出定长滑窗。 
            s -= nums[i - k + 1]
        
        # 最后返回符合题意的答案。 
        return max_s / k 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.01 00:34 

# 未通过代码 

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        ans = -inf 

        for i in range(n):
            left = i - k + 1
            
            if left < 0:
                continue
            
            ans = max(ans, sum(nums[left : (i + 1)]) / k)
            # 问题在于 切片要O(k)拷贝，sum要O(k)遍历，外层还有O(n)循环，时间复杂度O(n * (k ^ 2))，会超出题目的时间限制。 

        return ans 
    
# 时间复杂度O(n * (k ^ 2)) 
# 空间复杂度O(1) 

# 2026.01.01 00:44 