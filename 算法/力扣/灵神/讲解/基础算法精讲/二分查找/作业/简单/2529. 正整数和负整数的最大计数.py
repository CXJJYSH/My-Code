class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        
        # 可以遍历，我自己用的方法是二分查找。
        
        for i in nums:
            neg = pos = 0
            if i < 0:
                neg += 1
            elif i > 0:
                pos += 1
        return max(neg, pos)
        
        # 自己的二分查找代码。

        nums.sort()
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= 0:
                right = mid - 1
            else:
                left = mid + 1
        if left < len(nums) and nums[left] == 0:
            neg = left 
            while left < len(nums) and nums[left] == 0:
                left += 1
            zero = left - neg
            pos = len(nums) - neg - zero
            return max(pos, neg)
        else:
            neg = left
            pos = len(nums) - left
            return max(pos, neg)
        
        # 灵神的简洁二分查找代码。
        # 学到了之前没见过的新函数bisect_left(a, b)和bisect_right(a, b)。
        # 使用前提是有序数组。（这道题为非递减数组）
        # 作用：前者返回a中第一个等于b的元素的索引，后者返回a中第一个大于b的元素的索引。 

        neg = bisect_left(nums, 0)
        pos = len(nums) - bisect_right(nums, 0)
        return max(neg, pos)