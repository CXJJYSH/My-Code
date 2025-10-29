class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        
        # 下面是我写的代码，没用，没有通过。
        
        '''
        ans = 0
        left = 0
        right = len(nums) - 1
        while x > 0 and left < len(nums) and right > -1:
            if nums[left] >= nums[right]:
                x -= nums[left]
                ans += 1
                nums.pop(left)
                left = 0
                right = len(nums) - 1
                if x < 0:
                    return -1
            else:
                x -= nums[right]
                ans += 1
                nums.pop(right)
                right -= len(nums) - 1
                left = 0
                if x < 0:
                    return -1
        return ans
        '''
        
        # 下面是有漏洞的代码，无法通过[5,6,7,8,9]测试用例。
        # 将ans初始化为0会导致外层和里层循环都结束后其实没找到符合要求的数组，但是最后的return语句仍然当作“找到了”进行return。
        
        '''
        target = sum(nums) - x
        if target < 0:
            return -1
        s = 0
        left = 0
        ans = 0
        for right, i in enumerate(nums):
            s += i 
            while s > target:
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, right - left + 1)
        return len(nums) - ans
        '''
        
        # 下面是正确的代码。
        # 需要初始化ans为-1，用于后面“是否找到”的条件判断。
        # 这段代码就能做到检查的目的，因为如果没有找到目标ans不会更新，而ans作为状态条件能实现return -1 的功能。

        target = sum(nums) - x
        if target < 0:
            return -1
        ans = -1 
        s = 0
        left = 0
        for right, i in enumerate(nums):
            s += i
            while s > target:
                s -= nums[left]
                left += 1
            if s == target:
                ans = max(ans, right - left + 1)
        return -1 if ans < 0 else len(nums) - ans

# 2025.10.29 16:21 用时00:47:51