# 首先要确定 < 时移动左指针，>= 时移动右指针。

def lower_bound(nums, target):
    left = 0
    right = len(nums) - 1 # 左闭右闭。
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left 

# 左闭右闭写法应该记住指针移动和停止位置的例题画面，根据举例移动规律进行指针的赋值编写。
# 这里因为时左闭右闭，所以要排除元素就应该跳过该元素，往后或往前进行指针赋值。

def lower_bound2(nums, target):
    left = 0
    right = len(nums) # 左闭右开。
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left 

# 左闭右开写法应该由左闭右闭写法的指针移动规律稍加调整进行记忆：
# 左闭右闭写法最后为[R, L]的位置关系，此时返回的是L，这一点需要举例进行实例化记忆。
# 左闭右开写法因为初始化时右指针向右移动了一位，所以指针结束移动时的位置关系应该是R向右移动一位和L重合。
# 所以此时不仅可以返回L，也可以返回R。

def lower_bound3(nums, target):
    left = -1
    right = len(nums) # 左开右开。
    while left < right - 1:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid
        else:
            right = mid
    return right # 或者left + 1。

# 左开右开写法的修改和左闭右开写法的修改同理。
# 在左闭右开写法R和L重叠的基础上，因为初始化左指针时向左移动了一位，所以指针结束移动时的位置关系是[L, R]。
# 此时R位于应该返回的答案位置，所以这种写法需返回R。 

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = lower_bound3(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lower_bound3(nums, target + 1) - 1
        return [start, end]
    
# 讲类上面定义的函数放到类下面也没有关系，只要保证在执行调用的代码之前就行。 
# 中等题 算术评级4 
# 看完讲解自己写一遍就过了，击败100%，太爽了。
# 2025.10.31 12:25 用时应该是一个多小时，上一题是11:11完成的。当然，这道题还包括看灵神视频的时间。 
# 2025.10.31 12:41 写完了笔记注释。 