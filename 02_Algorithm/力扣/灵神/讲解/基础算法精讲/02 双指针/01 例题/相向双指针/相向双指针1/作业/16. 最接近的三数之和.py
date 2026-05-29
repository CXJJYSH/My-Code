from math import inf 

class Solution:
    def threeSumClosest1(self, nums: list[int], target: int) -> int:
        #第一段代码是我自己写的，也没有优化，直接就是按最基础的逻辑写的。
        ans = 0
        dis = float('inf')
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == target:
                    return s #而写return s就能过，甚至还打败了60.88%。
                    # ans = s 这里如果这样写的话就会超出时间限制，我现在还不知道是为什么。
                elif s < target:
                    tmp = abs(s - target)
                    if tmp <= dis:
                        dis = tmp
                        ans = s
                    left += 1
                else:
                    tmp = abs(s - target)
                    if tmp <= dis:
                        dis = tmp
                        ans = s 
                    right -= 1 
        return ans
    def threeSumClosest2(self, nums: list[int], target: int) -> int:
        #第二段代码是根据灵神的题解写的，break优化的细节写法和最后return ans时return的位置是回看了题解才写准确的。
        nums.sort()
        n = len(nums)
        min_diff = inf
        ans = 0
        for i in range(n - 2):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            s = nums[i] + nums[i + 1] + nums[i + 2]
            if s > target:
                if s - target < min_diff: 
                    ans = s #这里只用保证答案更新了就可以，不用更新中间的状态变量。
                break
            
            s = nums[i] + nums[-1] + nums[-2]
            if s < target:
                if target - s < min_diff:
                    min_diff = target - s 
                    ans = s 
                continue 
            
            j = i + 1
            k = n - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if s == target:
                    return s 
                elif s < target:
                    if target - s < min_diff:
                        min_diff = target - s 
                        ans = s 
                    j += 1
                    while nums[j] == nums[j - 1]: #这里的while优化是我根据灵神之前讲的自己加的。
                        j += 1
                else:
                    if s - target < min_diff:
                        min_diff = s - target 
                        ans = s 
                    k -= 1
                    while nums[k] == nums[k + 1]: #这里的while优化是我根据灵神之前讲的自己加的。
                        k -= 1
        return ans 
# 2025.10.15