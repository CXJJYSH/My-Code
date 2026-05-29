from typing import List


# 其实这两中滑窗的写法都是右指针右移导致窗口和变大，左指针要左移使窗口值小于（小于等于）某个值， 
# 只不过越长越合法型是 往左 统计符合条件的答案个数，越短越合法型是 往右 统计答案个数。 
# 而左右指针都只从左往右移一遍，所以时间复杂度为O(n)。 

# 大于等于 写法 

# 越长越合法 型 

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def betterThanOrEqual(k):
            ans = 0
            s = 0
            left = 0
            
            for right, x in enumerate(nums):
                s += x
            
                while left <= right and s >= k: # 测试的时候出现了left越界的问题，我这里就加了一个边界控制 left <= right 。 
                    s -= nums[left] 
                    left += 1
            
                ans += left 
            
            return ans 
        
        return betterThanOrEqual(goal) - betterThanOrEqual(goal + 1) 
        # 大于等于 goal 的比大于等于 goal + 1 的更多，所以要用solve(goal) - solve(goal + 1)。 

# 小于 写法（小于等于 写法） 

# 越短越合法 型 

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def lessThan(k):
            ans = 0
            s = 0
            left = 0
            
            for right, x in enumerate(nums):
                s += x
            
                while left <= right and s >= k:
                    s -= nums[left] 
                    left += 1
                ans += right - left + 1
            
            return ans 
        
        return lessThan(goal + 1) - lessThan(goal) 
        # 小于 goal + 1 的即小于等于 goal 的，小于 goal 的即小于等于 goal - 1 的。 
        # 所以用前者减后者。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.02.03 17:41 