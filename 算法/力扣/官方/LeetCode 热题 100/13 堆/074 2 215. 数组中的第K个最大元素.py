from random import randint
from typing import List

# 快速排序写法 

# 堆在哪里？ 

class Solution:
    def partition(self, nums, left, right):
        i = randint(left, right)
        pivot = nums[i]
        nums[i], nums[left] = nums[left], nums[i]

        i, j = left + 1, right 
        while True:
            while i <= j and nums[i] < pivot:
                i += 1
            
            while i <= j and nums[j] > pivot:
                j -= 1

            if i >= j:
                break

            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        nums[left], nums[j] = nums[j], nums[left]
        
        return j 

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        target_index = n - k 
        
        left, right = 0, n - 1
        while True:
            i = self.partition(nums, left, right)
            if i == target_index:
                return nums[i]
            if i > target_index:
                right = i - 1
            else: 
                left = i + 1

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.05.21 17:19 

# 库函数写法 

# 啊，这是C++的。 

# class Solution {
# public:
#     int findKthLargest(vector<int>& nums, int k) {
#         ranges::nth_element(nums, nums.end() - k);
#         return nums[nums.size() - k];
#     }
# };

# 2026.05.21 17:20 