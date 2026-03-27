from typing import Counter, List

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(nums1, nums2):
            nums1.sort()
            nums2.sort()
            
            cnt = Counter(nums2)
            
            ans = 0
            
            n = len(nums2)
            for i in range(len(nums1)):
                target = nums1[i] * nums1[i]
            
                left = 0
                right = n - 1
                while left < right:
                    m = nums2[left] * nums2[right] 
            
                    if m > target:
                        right -= 1
                    elif m < target:
                        left += 1
                    else:
                        # 统计 
                        if nums2[left] == nums2[right]:
                            ans += (cnt[nums2[left]] * (cnt[nums2[left]] - 1) // 2)
                            # 这里是所有相同元素取两个，用组合数公式做。 
                        else:
                            ans += (cnt[nums2[left]] * cnt[nums2[right]])
                            # 这里是两组元素个数相乘，可以同时统计重复和不重复的情况。 
                        
                        # 移动指针，跳过重复元素，重复就移动多次，不重复只会移动一次。 
                        left += 1
                        while left < right and nums2[left] == nums2[left - 1]:
                            left += 1
                        right -= 1
                        while left < right and nums2[right] == nums2[right + 1]:
                            right -= 1
            
            return ans 
       
        return count(nums1, nums2) + count(nums2, nums1)
    
# 2026.03.27 12:08 

# 时间复杂度O(n ^ 2) 
# 空间复杂度O(n) 

# 2026.03.27 14:39 