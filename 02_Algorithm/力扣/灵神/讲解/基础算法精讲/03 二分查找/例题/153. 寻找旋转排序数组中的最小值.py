class Solution:
    def findMin(self, nums: list[int]) -> int:
        
        # 依旧可以只遍历第一个元素到倒数第二个元素。
        
        # 左开右开
        
        left = -1
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid # 向最小值逼近。
            else:
                left = mid # 向最小值逼近。
        return nums[right] # 左开右开写法返回右指针。
        
        # 左闭右开
        
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid # 向最小值逼近。
            else:
                left = mid + 1 # 向最小值逼近。
        return nums[left] # 左闭右开写法返回左右指针都行。
        
        # 左闭右闭

        left = 0
        right = len(nums) - 2
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid - 1 # 向最小值逼近。
            else:
                left = mid + 1 # 向最小值逼近。
        return nums[left] # 左闭右闭写法返回左指针。