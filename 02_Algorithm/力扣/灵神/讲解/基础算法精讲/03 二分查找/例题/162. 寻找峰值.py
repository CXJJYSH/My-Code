class Solution:
    def findPeakElement(self, nums: list[int]) -> int:

        # 遍历第一个元素到倒数第二个元素。 
        
        # 这是左开右开区间写法。
        
        left = -1
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid
        return right
    
        # 这是左闭右闭区间写法。
    
        left = 0
        right = len(nums) - 2
        while left < right + 1:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
        # 这是左闭右开写法。
    
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

# 牛逼，自己写一遍都过了。

# 噢，我知道了————
# 要使区间不为空，
# 左开右开就要left + 1 < right;
# 左闭右开就要left < right;
# 左闭右闭就要left <= right,也是left < right + 1。 
# 且和其它条件无关。 

# 指针返回规律————
# 左闭右闭返回左指针，
# 左闭右开返回左右指针皆可，
# 左开右开返回右指针。