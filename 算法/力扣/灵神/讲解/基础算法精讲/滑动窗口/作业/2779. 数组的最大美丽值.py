class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        # “由于选的是子序列，且操作后子序列的元素都相等，所以元素顺序对答案没有影响，可以先对数组排序。”我现在还不理解为什么可以排序、以及排序后用滑动窗口找出来的数组就刚好全是符合要求的、且没有任何遗漏。
        
        # 奥！他是要找最大值呀，那子数组长度小一点对最大的答案就不影响了。

        # 这是灵神的方法。我自己没想出来，而且现在也还没完全理解。
        
        nums.sort()
        ans = 0
        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 2 * k:
                left += 1
            ans = max(ans, right - left + 1)
        return ans