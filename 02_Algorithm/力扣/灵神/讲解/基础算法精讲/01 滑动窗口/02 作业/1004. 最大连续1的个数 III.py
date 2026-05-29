class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        
        #上面是我的代码，下面是灵神的代码。

        ans = 0
        cnt = 0
        left = 0
        for right, i in enumerate(nums):
            if i == 0:
                cnt += 1
            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
        
        # 灵神的代码太优雅了。
        
        ans = 0
        cnt = 0
        left = 0
        for right, i in enumerate(nums):
            cnt += 1 - i
            while cnt > k:
                cnt -= 1 - nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans