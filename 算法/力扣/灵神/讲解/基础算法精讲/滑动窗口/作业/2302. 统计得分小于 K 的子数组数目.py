class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:

        # 我自己想到的基础滑窗实现是没问题的，在个数计算的时候有问题。
        
        # 没有和昨天的“越长越合法”类型的题目联系起来，没有看出这是“越短越合法”类型的题目，所以少了计算答案个数的细节。
        
        # 而且看了题解之后意识到了这是“越短越合法”类型的题目之后，个数计算还没有考虑周全，少了最小单位的情况。最后运行错误看完了题解代码之后才意识过来。
        
        # 虽然这道题用时00:25:05较短，但是仍应该郑重重视。

        ans = 0
        left = 0
        sum = 0
        for right, i in enumerate(nums):
            sum += i 
            while sum * (right - left + 1) >= k:
                sum -= nums[left]
                left += 1
            ans += (right - left + 1)
        return ans

# 困难题。1808分。
# 2025.10.28 17:47 用时00:25:05。