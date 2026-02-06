from collections import defaultdict
from typing import List


# 我的代码 

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        cnt = defaultdict(int)
        
        for right, x in enumerate(nums):
            cnt[x] += 1
            
            while cnt[x] > 1:
                out = nums[left]
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out] 
                left += 1
            
            ans = max(ans, sum(nums[left:right + 1]))
        
        return ans 
    
# 因为有可能整个nums数组的元素都不一样，这样外层循环每循环一次都会有(right + 1) ^ 2的操作数，总操作数为n ^ 3级，所以 
# 时间复杂度O(n ^ 3) 
# 因为有可能nums数组中的元素都不一样，cnt最多会存储n个元素，所以 
# 空间复杂度O(n) 

# 2026.01.04 18:21 

# 灵神的代码 布尔数组写法 

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        has = [False] * (max(nums) + 1)
        ans = 0
        left = 0 
        s = 0
        
        for x in nums:
            while has[x]:
                out = nums[left] 
                has[out] = False
                s -= out 
                left += 1
            # 如果检查到要进入哈希数组的元素已经在哈希数组中有True的值了， 
            # 那么就要先把左边的元素逐个清除， 
            # 把对应值改成False， 
            # 把和也做减法更新，
            # 直到布尔数组中新元素对应的值为False为止。

            has[x] = True
            # 然后把新元素记录进去，方式为把布尔值从False改成True。 

            s += x
            # 更新和。 

            ans = max(ans, s)
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.01.04 19:00 

# 灵神的代码 哈希集合写法 

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        st = set()
        ans = 0
        left = 0
        s = 0
        
        for x in nums:
            while x in st:
                out = nums[left] 
                st.remove(out)
                s -= out 
                left += 1
            # 先检查新元素是否在哈希集合里，如果在就要逐个将左边的元素移除出哈希集合，然后更新和，以及left下标。 

            st.add(x)
            # 然后把新元素加入哈希集合中。 

            s += x
            # 更新和。 

            ans = max(ans, s)
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.01.04 19:04 

# 如果是要统计子数组元素和的问题，那么更应该采用用s动态记录当前子数组元素和的方法，这种方法时间复杂度更低，而且只用了O(1)的额外变量。 
# 而不是用sum()内置函数，因为sum()内置函数的时间复杂度为O(n)，这里在循环内用sum()会提高代码整体的时间复杂度。 

# 2026.01.04 19:10 