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
            if left == len(nums) or nums[left] != target: # 灵神那里用的是开区间，开区间初始状态right就等于len(nums)，所以最后检查的时候是检查right是否等于len(nums)，即检查右指针有没有移动过。
                return -1                                 # 而我这里用的闭区间，却还是检查right是否等于len(nums)，错误应该就出在这里。我应该检查右指针有没有移动过，即right是否等于len(nums) - 1。
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

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def is_blue(i: int) -> bool:
            end = nums[-1]
            if nums[i] > end:
                return target > end and nums[i] >= target 
            else:
                return target > end or nums[i] >= target 
        left = -1
        right = len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid
            else:
                left = mid
        if right == len(nums) or nums[right] != target:
            return -1
        return right 
    
# 这是灵神的一次二分的写法，我今天看一遍看懂了之后复刻了一遍。
# 2025.11.05 16:30 
# 这个就是灵神一次二分的写法二，用了一个新函数。
# 2025.11.05 17:31

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = -1
        right = len(nums) - 1 # 这里赋len(nums)或len(nums) - 1都行。
        while left + 1 < right:
            mid = (left + right) // 2
            x = nums[mid]
            if target > nums[-1] >= x:
                right = mid
            elif x > nums[-1] >= target:
                left = mid
            elif x >= target:
                right = mid
            else:
                left = mid
        return right if nums[right] == target else -1
    
# 这又是灵神的没用新函数的一次二分的写法一。
# 2025.11.05 17:27 