from typing import List

# 2025.09.30 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        '''

        idx = {}
        for j, x in enumerate(nums): #前是索引后是值。
            if target - x in idx:
                return [idx[target - x], j]
            idx[x] = j 

# 2026.06.02 22:21 

# 哈希表写法 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for j, x in enumerate(nums):
            if target - x in index:
                return [index[target - x], j] 
            
            index[x] = j 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.06.02 22:25 