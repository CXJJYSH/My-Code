class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        ans = n + 1
        left = 0
        s = 0
        for right, num in enumerate(nums):
            s += num 
            while s - nums[left] >= target:
                s -= nums[left]
                left += 1
            if s >= target:
                ans = min(ans, right - left + 1)
        
            # 不能直接ans取最小值，引文上面的while循环不一定会进行且s也不一定大于等于target，有可能出现没有符合条件的子数组的情况，这时候直接取最小值返回是错误的。
        
            ans = min(ans, right - left + 1)
        
        return ans if ans <= n else 0
        
        n = len(nums)
        ans = n + 1
        s = 0
        left = 0
        for right, num in enumerate(nums):
            s += num
            # 这里的while循环内的逻辑也要明确，应该是大于等于时就立即更新ans，
            # 然后再更新s和left，为了之后的循环条件判断、以及防止left提前更新使结果计算错误。
            while s >= target:
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1
        return ans if ans <= n else 0