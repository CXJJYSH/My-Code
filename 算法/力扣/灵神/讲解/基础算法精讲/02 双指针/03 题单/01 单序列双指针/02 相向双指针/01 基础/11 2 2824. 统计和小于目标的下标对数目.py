from typing import List

# 2025.10.15 做的第一遍的答案。

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        #最基础的方法——循环遍历
        '''
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                if s < target:
                    ans += 1
        return ans
        '''
        #改进方法——相向双指针
        ans = 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                ans += right - left #这里的数量关系可以举三个数的符合条件的数组为例。
                left += 1
            else:
                right -= 1
        return ans
        #用改进后的方法时间复杂度就击败100%了😂。

# 2026.03.20 第二遍的代码。 

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        ans = 0
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] < target:
                ans += right - left 
                left += 1
            else:
                right -= 1
        
        return ans 
    
# 第二遍做这道题竟然在统计答案的地方出错了，我本来写的是ans += left + 1，这个逻辑有问题，会少算答案。 
# 比如 0, 1, 2, 3 ，target = 4 ，第一次统计应该为 ans += 3 - 0 ，而不是 ans += 0 + 1，前者才是对的。 
# 只能用 ans += right - left 来统计。 

# 当是找小于的时候，每次统计时固定向增大方向移动的指针，统计两个指针之间的数对数，然后移动向增大方向移动的指针； 
# 当是找大于的时候，每次统计时固定向减小方向移动的指针，统计两个指针之间的数对数，然后移动向减小方向移动的指针。 

# 没想到这道算术评级为1的之前做过的简单题还能卡我这么久。 

# 2026.03.20 12:15 