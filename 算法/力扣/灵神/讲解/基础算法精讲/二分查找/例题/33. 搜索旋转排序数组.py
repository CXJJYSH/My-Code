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