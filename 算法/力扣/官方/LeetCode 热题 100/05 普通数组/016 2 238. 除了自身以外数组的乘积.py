from typing import List

# 第一段是我自己写的代码，用两个数组分别存前面一段和后面一段的乘积，根据情况选择相乘即可。 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        
        left = []
        right = []
        
        cnt_left = 1
        cnt_right = 1
        
        for i in range(len(nums)):
            cnt_left *= nums[i]
            left.append(cnt_left)
        
        for j in range(len(nums) - 1, -1, -1):
            cnt_right *= nums[j]
            right.append(cnt_right)
        
        for k in range(len(nums)):
            if k == 0:
                ans.append(right[len(nums) - 2])
            elif k == len(nums) - 1:
                ans.append(left[len(nums) - 2])
            else:
                ans.append(left[k - 1] * right[len(nums) - k - 2])
        
        return ans 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.04.16 14:38 耗时9:09。 

# 灵神的写法一 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        pre = [1] * n 
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1] # i从1开始，从nums[0]开始存，存到nums[n - 2]，不存nums[n - 1]。 
        
        suf = [1] * n 
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1] # i从n - 2开始，从nums[n - 1]开始存，存到nums[1]，不存nums[0]。 
        
        return [p * s for p, s in zip(pre, suf)]
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.04.16 15:31 

# 灵神写法空间优化版 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) 

        suf = [1] * n 
        for i in range(n - 2, -1 , -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        pre = 1
        for i, x in enumerate(nums):
            suf[i] *= pre # 先乘pre再更新pre得到的刚好就是正确答案。刚好suf[0]即为答案[0]，不需要乘前缀，只要乘个1。 
            pre *= x 

        return suf 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.16 15:37 