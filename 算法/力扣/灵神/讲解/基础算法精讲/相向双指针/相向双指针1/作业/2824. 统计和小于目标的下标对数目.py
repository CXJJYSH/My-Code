class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        #最基础的方法——循环遍历
        '''
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                if s < target:
                    ans += 1
        return ans
        '''
        #改进方法——相向双指针
        ans = 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                ans += right - left #这里的数量关系可以举三个数的符合条件的数组为例。
                left += 1
            else:
                right -= 1
        return ans
        #用改进后的方法时间复杂度就击败100%了😂。
# 2025.10.15