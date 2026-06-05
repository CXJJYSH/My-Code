from typing import List

# 2025.10.14 
# 2026.03.22 

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
    
# 2026.06.05 10:52 

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() 

        ans = [] 
        
        n = len(nums)
        
        for i in range(n - 2):
            x = nums[i] 
            
            if i > 0 and x == nums[i - 1]:
                continue 
            if x + nums[i + 1] + nums[i + 2] > 0:
                break 
            if x + nums[-1] + nums[-2] < 0:
                continue 
            
            j = i + 1
            k = n - 1 

            while j < k:
                s = x + nums[j] + nums[k]

                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return ans 
    
# 时间复杂度O(n ** 2) 
# 空间复杂度O(1) 

# 2026.06.05 11:00 