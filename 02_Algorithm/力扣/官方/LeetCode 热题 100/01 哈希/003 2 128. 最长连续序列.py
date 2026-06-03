from typing import List

# 2025.10.01 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        '''
        st = set(nums)
        ans = 0
        for x in st:
            if x - 1 in st:
                continue
            y = x + 1
            while y in st:
                y += 1
            ans = max(ans, y - x) #活用数量关系
        return ans
        '''

        st = set(nums)
        m = len(st)
        ans = 0
        for x in st:
            if x - 1 in st:
                continue
            y = x + 1
            while y in st:
                y += 1
            ans = max(ans, y - x)
            '''
            if ans * 2 >= m:
                return ans #TM我这里直接return后面不写return在nums = []的时候根本就不会进入循环，因为根本找不到一个元素，最后直接因为到达不了return语句而啥也不会返回，只会返回null。所以要先break，然后再跳出循环return ans。
            '''
            if ans * 2 >= m:
                break
        return ans 

# 2026.06.03 12:55 

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums) # 创建一个集合。 

        ans = 0
        
        for x in st:
            if x - 1 in st:
                continue # 有前序元素就剪枝。 
        
            y = x + 1 
            while y in st:
                y += 1

            ans = max(ans, y - x) # x 到 y - 1 共 y - x个元素。 
            # if ans * 2 >= len(st):  # ans 不可能变得更大
            #     break
            # 这里可以加入剪枝。 

        return ans 
        
# 时间复杂度O(n)，二重循环每个元素最多遍历两次，外层一次内层一次，因为如果和其它连续了之前就遍历了现在就跳过了。 
# 空间复杂度O(len(st)) 

# 2026.06.03 13:00 

# 2026.06.03 13:03 