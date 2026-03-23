from cmath import inf
from typing import List

# 2026.10.15 第一次的代码 

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #第一段代码是我自己写的，也没有优化，直接就是按最基础的逻辑写的。
        '''
        ans = 0
        dis = float('inf')
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == target:
                    return s #而写return s就能过，甚至还打败了60.88%。
                    # ans = s 这里如果这样写的话就会超出时间限制，我现在还不知道是为什么。
                elif s < target:
                    tmp = abs(s - target)
                    if tmp <= dis:
                        dis = tmp
                        ans = s
                    left += 1
                else:
                    tmp = abs(s - target)
                    if tmp <= dis:
                        dis = tmp
                        ans = s 
                    right -= 1 
        return ans
        '''
        nums.sort()
        n = len(nums)
        min_diff = inf
        ans = 0
        for i in range(n - 2):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            s = nums[i] + nums[i + 1] + nums[i + 2]
            if s > target:
                if s - target < min_diff: 
                    ans = s #这里只用保证答案更新了就可以，不用更新中间的状态变量。
                break
            
            s = nums[i] + nums[-1] + nums[-2]
            if s < target:
                if target - s < min_diff:
                    min_diff = target - s 
                    ans = s 
                continue 
            
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s 
                elif s < target:
                    if target - s < min_diff:
                        min_diff = target - s 
                        ans = s 
                    j += 1
                    while nums[j] == nums[j - 1]: #这里的while优化是我根据灵神之前讲的自己加的。
                        j += 1
                else:
                    if s - target < min_diff:
                        min_diff = s - target 
                        ans = s 
                    k -= 1
                    while nums[k] == nums[k + 1]: #这里的while优化是我根据灵神之前讲的自己加的。
                        k -= 1
        return ans 
    
# 2026.03.23 我第二次做的时候没自己写出来，GPT帮我改了。 

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')  # 使用浮动的正无穷来初始化
        for i in range(len(nums) - 2):  # 只需要遍历到 len(nums) - 2
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < abs(ans - target):  # 更新条件
                    ans = s
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    break
        return ans
    
# 本来是这样的，我不知道为什么过不了。 

class Solution: 
    def threeSumClosest(self, nums: List[int], target: int) -> int: 
        nums.sort() 
        ans = 0 
        for i in range(len(nums)): 
            dis = inf 
            left = i + 1 
            right = len(nums) - 1 
            while left < right: 
                s = nums[i] + nums[left] + nums[right] 
                if abs(s - target) < dis: 
                    ans = s 
                    dis = abs(s - target) 
                    if s > target: 
                        right -= 1 
                    elif s < target: 
                        left += 1 
                    else: 
                        break 
                else: 
                    if s > target: 
                        right -= 1 
                    else: 
                        left += 1 
        return ans

# 啊，我真无语了，这样一道题总共提交了超级多遍，这么卡的吗 

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        ans = inf 
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
        
            while left < right:
                s = nums[i] + nums[left] + nums[right]
        
                if s == target: 
                    return target 
        
                if abs(s - target) < abs(ans - target):
                    ans = s 
        
                if s > target:
                    right -= 1
                else:
                    left += 1
    
        return ans 
    
# 时间复杂度O(n ^ 2)，nums.sort()为O(n log n)，双层循环为O(n ^ 2)，总的为O(n ^ 2)。 
# 空间复杂度O(1)，忽略排序的栈开销，返回值不计入。 

# 2026.03.23 23:45 