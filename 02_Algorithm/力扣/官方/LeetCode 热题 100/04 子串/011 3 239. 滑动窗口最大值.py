from collections import deque
from typing import List

# 都是灵神的写法 

# 2025.12.30 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        q = deque()
        for i, x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)
            if i - q[0] + 1 > k:
                q.popleft()
            if i >= k - 1:
                ans.append(nums[q[0]])
        return ans 
    
# 2026.04.15 11:44 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * (len(nums) - k + 1)
        q = deque()

        for i, x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()

            q.append(i)

            left = i - k + 1
            if q[0] < left:
                q.popleft()
            
            if left >= 0:
                ans[left] = nums[q[0]]
        
        return ans 
    
# 灵神的题解 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * (len(nums) - k + 1)  # 窗口个数
        q = deque()  # 双端队列

        for i, x in enumerate(nums):
            # 1. 右边入
            while q and nums[q[-1]] <= x:
                q.pop()  # 维护 q 的单调性
            q.append(i)  # 注意保存的是下标，这样下面可以判断队首是否离开窗口

            # 2. 左边出
            left = i - k + 1  # 窗口左端点
            if q[0] < left:  # 队首离开窗口
                q.popleft()

            # 3. 在窗口左端点处记录答案
            if left >= 0:
                # 由于队首到队尾单调递减，所以窗口最大值就在队首
                ans[left] = nums[q[0]]

        return ans
    
# 时间复杂度O(n)，左右指针各遍历O(n)遍，每个下标最多出入各一次。 
# 空间复杂度O(min(k, U))，U为nums不同元素个数，q存的最大数目就是空间复杂度。 

# 空间复杂度确实如上面这样，不同情况下min取决于k或U。 

# 2026.04.15 11:51 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * (len(nums) - k + 1)
        q = deque() 

        for i, x in enumerate(nums):
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(i)

            left = i - k + 1
            if q[0] < left:
                q.popleft()
            
            if left >= 0:
                ans[left] = nums[q[0]] 
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(min(k, U)) 
    
# 2026.06.11 16:47 