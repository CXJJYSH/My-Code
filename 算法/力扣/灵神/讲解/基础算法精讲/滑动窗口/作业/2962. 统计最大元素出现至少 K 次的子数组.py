# “越长越合法”型滑动窗口

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        
        # 我的代码超出时间限制了😢。写了二十多分钟，快三十分钟了。
        
        ans = 0
        max_value = max(nums)
        num = 0
        for right, i in enumerate(nums):
            left = 0
            if i == max_value:
                num += 1
            cnt = num
            while cnt >= k:
                ans += 1
                if nums[left] == max_value:
                    cnt -= 1
                left += 1
        return ans
        
        # 这是自己看了灵神的题解后自己写的代码。超过了74.02%。
        
        mx = max(nums)
        ans = 0
        cnt = 0
        left = 0
        for right, i in enumerate(nums):
            if i == mx:
                cnt += 1
            while cnt == k:
                if nums[left] == mx:
                    cnt -= 1
                left += 1
            ans += left
        return ans
        
        # 这是灵神的代码。超过了93.48%。
        
        mx = max(nums)
        ans = 0
        cnt = 0
        left = 0
        for i in nums:
            if i == mx:
                cnt += 1
            while cnt == k:
                if nums[left] == mx:
                    cnt -= 1
                left += 1
            ans += left # 灵神的代码太优雅了，竟然可以通过这样的一个巧妙计算算出正确答案。越长越合法型滑动窗口题原来可以这样做。
        return ans
    
# 思考题

# 改成子数组的最大值在子数组中至少出现 k 次，要怎么做？（原题是整个数组的最大值，这里是子数组的最大值）

# 欢迎在评论区分享你的思路/代码。

# 提示：907. 子数组的最小值之和