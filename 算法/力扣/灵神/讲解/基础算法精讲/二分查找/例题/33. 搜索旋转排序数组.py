class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # 找旋转点（最小值下标）
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        rot = left
        # 重新设定左右边界做正常二分
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            realmid = (mid + rot) % len(nums) # 这是GPT的写法，竟然用到了取模，我没想到这里竟然可以用取模。 
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = -1
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid 
            else:
                left = mid 
        if target <= nums[-1]:
            left, right = right - 1, len(nums)
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid
                else:
                    right = mid
            return right
        else:
            left = -1
            while left + 1 < right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid 
                else:
                    right = mid
            return right

# 这一段是废弃代码，上完体育课回寝室敲了一通发现没过，看了一下题解也不知道怎么改。今天就先这样吧，不在这道题上耗着了，明天再来重新想。
# 2025.11.03 16:48

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid - 1
            else:
                left = mid + 1
        min_number = left 
        if target > nums[-1]:
            left = 0
            right = min_number - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            if nums[left] != target:
                return -1
            return left
        else:
            left = min_number
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            if left == len(nums) or nums[left] != target:
                return -1
            return left
        
# 上面又是我第二天写的没过代码，关键是我现在还不知道我的代码哪里出了问题。 
# 2025.11.04 15:49
        
class Solution:

    def findMin(self, nums: list[int]) -> int:
        left = -1
        right = len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid 
            else:
                left = mid 
        return right

    def lower_bound(self, nums, left, right, target):
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target: # 真牛逼，我这里抄着抄着竟然把target抄成right了，我真服了，虽然是我自己想要复现的，但是敲的时候竟然敲错了。
                right = mid
            else:
                left = mid
        return right if nums[right] == target else -1

    def search(self, nums: list[int], target: int) -> int:
        i = self.findMin(nums)
        if target > nums[-1]:
            return self.lower_bound(nums, -1, i, target)
        return self.lower_bound(nums, i - 1, len(nums), target)
    
# 上面这段是灵神的两次二分的代码，我照着抄的竟然没过，现在还不知道是为什么。 
# 好了，修改了之后就通过了。灵神还是太屌了。
# 2025.11.04 17:03 

class Solution:
    # 153. 寻找旋转排序数组中的最小值（返回的是下标）
    def findMin(self, nums: list[int]) -> int:
        left, right = -1, len(nums) - 1  # 开区间 (-1, n-1)
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid
        return right

    # 有序数组中找 target 的下标
    def lower_bound(self, nums: list[int], left: int, right: int, target: int) -> int:
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            # 循环不变量：
            # nums[right] >= target
            # nums[left] < target
            if nums[mid] >= target:
                right = mid  # 范围缩小到 (left, mid)
            else:
                left = mid  # 范围缩小到 (mid, right)
        return right if nums[right] == target else -1

    def search(self, nums: list[int], target: int) -> int:
        i = self.findMin(nums)
        if target > nums[-1]:  # target 在第一段
            return self.lower_bound(nums, -1, i, target)  # 开区间 (-1, i)
        # target 在第二段
        return self.lower_bound(nums, i - 1, len(nums), target)  # 开区间 (i-1, n)
    
# 上面这段是灵神的题解原代码。
# 2025.11.04 17:03 
# 一次二分的写法就明天再来看吧，今天光写好两次二分的代码就花费了两个小时了。