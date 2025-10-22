class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        
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
# 2025.10.16