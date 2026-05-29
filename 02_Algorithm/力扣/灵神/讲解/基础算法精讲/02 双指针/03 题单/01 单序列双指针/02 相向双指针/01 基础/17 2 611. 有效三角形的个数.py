from typing import List

# 2025.10.16 写的 

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        #我自己想只能想出一半的代码，想完整写出来不可能。后来看了一下灵神的题解，受到启发，写出了完整的代码。但是还是和灵神的有点差别，我一开始就用的倒序遍历，灵神一开始用的是正序遍历。
        #学到的技巧是想要正常无误地往一个方向遍历，就要明确单个指针移动的单个方向。
        
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += right - left 
                    right -= 1
                else:
                    left += 1
        return ans 
        
        #第二段是看完灵神的最基础的写法之后自己复刻了一下 。
        
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(2, n):
            left = 0
            right = i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1
        return ans 
        
        #第三段是复刻了灵神的优化写法。
        
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n - 1, 1, -1):
            if nums[0] + nums[1] > nums[i]:
                ans += (i + 1) * i * (i - 1) // 6 #2 复刻过程中这里的数量关系我扩大范围了.
                break
            if nums[i - 1] + nums[i - 2] <= nums[i]:
                continue
            left = 0
            right = i - 1 #1 最开始我这里还写成了n - 1。
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += right - left #3 我这里忘记正确的数量可能不止一个，一开始写成1了。
                    right -= 1
                else:
                    left += 1
        return ans #上面的三个错误都是在解答错误后回看题解纠正过来的。
        
# 2026.03.25 23:36 

# 2026.03.26 第二遍写的代码 

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        ans = 0
        
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
        
            while left < right:
                if nums[i] + nums[left] > nums[right]: 
                    ans += right - left 
                    left += 1 
                else:
                    right -= 1
        
        return ans 
    
# 我这里一开始用的正序枚举最短边，会有遗漏的情况。 
# 而灵神用倒序枚举最长边就没有遗漏的情况。 

# 一改成倒序枚举最长边就通过了。 

# 我这里倒序枚举最长边，用最小两边之和大于第三边，可以用相向双指针。 
# 而正序枚举最短边，用最大两边之差相遇第三边，可以用同向双指针。 

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        ans = 0
        
        for i in range(2, len(nums)):
            left = 0
            right = i - 1
        
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += right - left 
                    right -= 1
                else:
                    left += 1
        
        return ans 
    
# 时间复杂度O(n ^ 2) 
# 空间复杂度O(1) 

# 同向双指针 
# 最大两边之差小于第三边 
# 正序枚举最短边 
# 三边紧挨着起始 

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort() 
        
        ans = 0
        
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                continue 
        
            j = i + 1
            for k in range(j + 1, len(nums)):
                while nums[k] - nums[j] >= nums[i]:
                    j += 1
        
                ans += k - j 
        
        return ans 
    
# 为什么这里没检验nums[i]是否为0索引就超出范围了？为什么枚举最短边要检验0，枚举最长边就不用？ 

# 和大于第三边，0永远不能和其它元素构成三角形，所以不会统计。 
# 差小于第三边，全是0会使j在while循环一直增大超出范围，所以要检验0直接continue，如果全是0直接跳出循环，直接返回 ans == 0 。 

# 2026.03.26 12:40 