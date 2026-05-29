from typing import List

# 这道题的关键在于跳过重复答案 
# 外层枚举要用if-continue跳过，内层枚举要用while跳过。 

# 2025.10.14 第一次写的代码 灵神的写法 

class Solution:
    def threeSum(self, nums: List[int]) -> List[list[int]]:
        nums.sort()
        
        ans = []
    
        n = len(nums)
        for i in range(n - 2):
            x = nums[i]
    
            if i > 0 and x == nums[i - 1]:
                continue
    
            if x + nums[i + 1] + nums[i + 2] > 0:
                break
    
            if x + nums[-2] + nums[-1] < 0:
                continue
    
            j = i + 1
            k = n - 1
            while j < k:
                s = x + nums[j] + nums[k]
    
                if s < 0:
                    j += 1
    
                elif s > 0:
                    k -= 1
    
                else:
                    ans.append([nums[i], nums[j], nums[k]])
    
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
    
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
    
        return ans
            
# 时间复杂度O(n ^ 2) 
# 空间复杂度O(1) 没考虑sort()算法。 

# 2026.03.22 第二次写的代码 GPT的写法 

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        ans = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            left = i + 1
            right = len(nums) - 1
        
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
        
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
        
                    left += 1
                    right -= 1
        
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
        
                else:
                    right -= 1
        
        return ans 
    
# 我知道为什么 
# 灵神是先移再while 
# GPT是先while再移了 
# 灵神从左向右移指针是用后一个与前一个比较，从右向左移是用前一个和后一个比较 
# GPT从左向右移指针是用前一个与后一个比较，从右向左移是用后一个和前一个比较 
# 灵神while结束后能达到当前元素和前一元素不相等的情况，先移一次也可能直接到第一个不相等的元素，所以要先移，移了之后还想等再while。 
# GPTwhile结束后不能达到当前元素和前一元素不相等的情况，只能达到相等元素中的最后一个元素，所以要再移一次指针。 

# 时间复杂度O(n ^ 2) 
# 空间复杂度O(1)，返回值不计入，忽略排序的栈开销。 

# 2026.03.22 22:49 