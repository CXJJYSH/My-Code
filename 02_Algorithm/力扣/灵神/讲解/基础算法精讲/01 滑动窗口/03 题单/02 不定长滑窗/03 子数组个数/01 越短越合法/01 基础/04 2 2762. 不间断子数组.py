from collections import deque
from typing import Counter, List

# 滑动窗口 + 集合/哈希表 写法 

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans = 0
        cnt = Counter()
        left = 0
        
        for right, x in enumerate(nums):
            cnt[x] += 1
            
            while max(cnt) - min(cnt) > 2: # 这里用计数字典统计元素可以直接消去题目条件中的绝对值符号。 
                
                # 但是max和min内置函数需要用到O(n)时间复杂度。
                # 因为这里cnt的最大值已经知道是一个常数 2 + 1 = 3 了，所以用D表示最大值最小值之差的上限，则时间复杂度为O(D)。 
                # 灵神说是O(D)，但是我感觉是O(D + 1)。 

                out = nums[left] 
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
                left += 1
            
            ans += right - left + 1
        
        return ans 

# 时间复杂度O(n * D) / 时间复杂度O(n * (D + 1)) 
# 空间复杂度O(D) / 空间复杂度O(D + 1) 

# 2026.01.25 11:54 

# 滑动窗口 + 单调队列 写法 

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        min_q = deque()
        max_q = deque()
        # 这里的deque()是创建双端队列的意思。 
        # 这里的双端队列保存的是元素索引。 
        # deque: double-ended queue 
        
        ans = 0
        left = 0
        
        for right, x in enumerate(nums):
            
            while min_q and x <= nums[min_q[-1]]:
                min_q.pop()
            min_q.append(right)
            # 将最小值队列更新成从最小值开始从小到大排列。 

            while max_q and x >= nums[max_q[-1]]:
                max_q.pop()
            max_q.append(right)
            # 将最大值队列更新成从最大值开始从大到小排列。 
            
            while nums[max_q[0]] - nums[min_q[0]] > 2:
                left += 1
                # 先滑动窗口，缩小窗口大小。 
                if min_q[0] < left:
                    min_q.popleft()
                # 如果最小值出去了，删除最小值的索引。 

                if max_q[0] < left:
                    max_q.popleft()
                # 如果最大值出去了，删除最大值的索引。 

            ans += right - left + 1
            # 更新答案。 

        return ans 
    
# 时间复杂度O(n)，这种写法就没有max()和min()这两个内置函数增加时间复杂度了。 
# 空间复杂度O(n) 

# 2026.01.26 17:56 