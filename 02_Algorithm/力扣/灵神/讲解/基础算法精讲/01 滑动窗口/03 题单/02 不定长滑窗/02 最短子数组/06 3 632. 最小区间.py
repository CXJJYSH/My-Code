from cmath import inf
from heapq import heapify, heapreplace
from typing import List

# 堆写法 

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        h = [(arr[0], i, 0) for i, arr in enumerate(nums)]
        heapify(h)

        ans_l = h[0][0]
        ans_r = max(arr[0] for arr in nums)
        r = max(arr[0] for arr in nums)
        
        while h[0][2] < len(nums[h[0][1]]) - 1: # while语句条件的含义：https://chatgpt.com/c/696273cb-74c0-832e-a2ab-f34ade66d5ea 
            _, i, j = h[0] 
            
            x = nums[i][j + 1]
            heapreplace(h, (x, i, j + 1))
            
            r = max(r, x)
            l = h[0][0]
            
            if r - l < ans_r - ans_l:
                ans_l, ans_r = l, r 
        
        return [ans_l, ans_r] 
    
# 这个堆的方式第一次见，还真挺难理解的，多看灵神的解析和GPT的讲解加深理解才好。 

# 时间复杂度O(L log n) 
# h是由二维数组nums的每一个一维数组的首元素的信息构成的，之后逐渐更新为各自的后续的元素，故h一共有n个元素，n为二维数组nums的长度。 
# L是nums中所有一维数组的长度之和，在while循环中用到O(L)的时间复杂度， 
# 在while循环中heapreplace需要用到O(log n)的时间复杂度来操作堆h， 
# 所以总体的时间复杂度为O(L log n) 

# 空间复杂度O(n) 
# 堆h需要O(n)的空间储存储每个一维数组的一个元素。 

# 2026.01.10 23:57 

# 2026.01.11 00:05 

# 滑动窗口写法 

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pairs = sorted((x, i) for i, arr in enumerate(nums) for x in arr) 
        # 这里的sorted是排序的意思。会影响后面的时间复杂度。 
        # 这里构建的元组列表每个元组的元素分别是nums中列表的元素值和nums中列表的索引。 
        # 后面也是一一对应的。 
        
        ans_l, ans_r = -inf, inf 
        
        empty = len(nums)
        cnt = [0] * empty # cnt是用来查找某个索引对应的列表中的元素出现次数是否大于或等于一的列表。 
        
        left = 0

        for r, i in pairs: # 先值，后索引。 
            if cnt[i] == 0:
                empty -= 1 # 这里是先处理边界条件，再更新。写代码的时候要灵活变通。 
            cnt[i] += 1
            
            while empty == 0:
                l, x = pairs[left] # 这里也可以改成 l, i ，效果是一样的，也不会出错，这是Python中特别的一个要注意的语法。 
                
                if r - l < ans_r - ans_l:
                    ans_l, ans_r = l, r 
                # 这里更新答案是用两边的端点值更新结果的区间端点，最后要返回一个区间。 
                
                cnt[x] -= 1 # 这里是先更新，再处理边界条件。写代码的时候要灵活变通。 
                if cnt[x] == 0:
                    empty += 1
                left += 1
        
        return [ans_l, ans_r] # 最后返回最小区间。 
    
# 时间复杂度O(L * log L)，L为所有nums[i]的长度之和。排序占用O(L * log L)的时间复杂度，循环不是瓶颈，瓶颈在排序上。使用归并可以做到O(L * log n)。 
# 空间复杂度O(L)，为pairs的长度。 

# 2026.01.24 00:20 