# 感觉很难理解的一道困难题。 

from bisect import bisect_left
from collections import defaultdict
from typing import List

class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        k = (n * (n + 1) // 2 + 1) // 2 # 这个是中位数的位置。 

        def check(upper: int) -> bool:
            # 这个函数传进的参数upper是表示窗口中不同元素的个数上限，值处于[1, len(set(nums)]范围内。 

            cnt = 0
            left = 0
            freq = defaultdict(int)
            # 用freq统计窗口中出现的不同元素。 
            # defaultdict()创建的就是字典，准确地说是字典dict的一个子类，本质还是字典dict，只是多了一个默认值机制。 

            for right, x in enumerate(nums):
                freq[x] += 1
                
                while len(freq) > upper:
                    # 用len(freq)表示不同的元素个数。 
                    
                    out = nums[left] 
                    freq[out] -= 1
                    if freq[out] == 0:
                        del freq[out] 
                    left += 1

                cnt += right - left + 1
                # 这里是在统计nums有多少个不同元素不超过当前个数上限的子数组。 

                if cnt >= k:
                    return True
                # 这里处理边界条件，一旦子数组个数超过了中位数的位置，就返回True，表示找到了中位数位置上存在的个数上限。 
                # 这里提前返回也相当于剪枝。 

            return False
            # 如果跑完了整个循环cnt都还没超过中位数的位置，那么就返回False，表示当前个数上限不足以找到超过中位数位置个数的子数组。 

        return bisect_left(range(len(set(nums))), True, 1, key = check)
    
# 整个check函数的逻辑就是对nums数组进行滑窗，统计不超过不同元素个数上限的子数组有多少个， 
# 一旦当前个数上限控制下找到了超过中位数位置上数字的子数组个数，就提前返回True，表示找到了 第一个 结果为True的个数上限。 

# 最后一句代码的意思是一个二分查找， 
# range(len(set(nums)))表示了二分查找的范围，准确来说是右边界，这里是区间
# True表示要找到逻辑返回结果为True的第一个个数上限， 
# 1表示也表示二分查找的范围，准确来说是左边界，从1开始，这里是闭区间， 
# key = check表示二分时并不直接操作范围内的数字，这里的范围内的数字表示的是不同的upper， 
# 这里是对不同的upper进行函数调用check(upper)，然后在按顺序得到的各个check(upper)结果组成的列表里进行二分， 
# 这里的结果列表只有False和True两种元素，且False全部在前面，True全部在后面。 
# 而返回的时候返回的一定是「没经过 check 的原始元素对应的位置」。 

# 一句话总结：bisect_left(range(...), True, 1, key=check)表示“在一个隐式序列 check(i) 中，从索引1开始，二分查找第一个等于 True 的位置。” 
# bisect_left为左侧插入，插入在第一个True前面，也是所有True前面，返回的是第一个True的位置， 
# bisect_right为右侧插入，插入在最后一个True后面，也是所有True后面，返回的是第一个不等于True的元素的位置。 
# GPT说：“你现在对bisect的理解，已经是可以安全写竞赛代码的水平了。” 

# 问题：为什么是True而不是1？ 
# 解答：x=True 和 x=1 在结果上是等价的，用 True 是为了语义清晰，不是因为语法必须。 
# 问题：和手写 while 二分的性能对比 
# 解答：时间复杂度完全一样，常数几乎没差，选顺手的。 

# while写法： 
# lo, hi = 1, len(set(nums))
# while lo < hi:
#     mid = (lo + hi) // 2
#     if check(mid):
#         hi = mid
#     else:
#         lo = mid + 1
# return lo

# 时间复杂度O(n * log n)，n为nums长度，二分O(log n)次，每次都要对nums数组进行O(n)的滑动窗口循环，综合为O(n * log n)。 
# 空间复杂度O(n)，为freq字典的空间复杂度。 

# 2026.01.27 20:37 