from cmath import inf
from typing import List

# 在while循环外更新答案的写法 

# 重新理解了一下这种写法就感觉还是挺好理解的，先加新元素，能缩小就缩小，然后满足条件的时候才更新，这样理解了就行。 

# 但是我感觉还是不如在while循环内更新答案的写法。 

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = inf 
        left = 0
        s = 0
        
        for right, x in enumerate(nums):
            s += x
            
            while s - nums[left] >= target:
                s -= nums[left] 
                left += 1
            # 这里只是在尽量缩小数组长度，没有更新答案的步骤。 

            if s >= target:
                ans = min(ans, right - left + 1)
                # 要更新就必须加条件，满足条件的时候才能更新。 
        
        return ans if ans <= n else 0 
        # 因为有可能整个循环结束了都没有达到满足 s >= target 的情况，而ans初始化成了比答案范围更大的数，没有经过更新直接返回会不符合题意， 
        # 所以要进行if - else判断，在答案范围内就直接返回，不在答案范围内则返回0。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.06 16:44 

# 在while循环内更新答案的写法 

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = inf 
        left = 0
        s = 0

        for right, x in enumerate(nums):
            s += x
            
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        
        return ans if ans <= n else 0 
    
# 我感觉这种写法就好理解得多，只要满足题目条件就更新答案，然后更新状态继续更新，一旦取了最小值最后就一定能更新成最小的答案。 
# 最后ans在答案范围内就直接返回ans，不在答案范围内则返回0。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.01.06 16:50 