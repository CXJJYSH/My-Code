from typing import List

# 这下面是我的写法，本来一开始是 right - left + 1 的，不行，可是不知道为什么改成 right - left 之后就可以了，竟然通过了。 
# 总共花了不到10分钟。 

# 现在我知道了，当最大元素加最小元素和符合条件之后，可以固定最小元素， 
# 最小元素之后一直到最大元素的元素都可以选或不选， 
# 本来最小最大这一段一共有 right - left + 1 个元素， 
# 现在固定了最小之后只有 right - left 个可选， 
# 所以 2 的次方要取 right - left 。 

# 我这个循环里用次方计算的方法速度之后8%多一点。 

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        ans = 0
        left = 0
        right = len(nums) - 1
        while left <= right: 
            s = nums[left] + nums[right]
            if s > target:
                right -= 1
            else:
                ans += 2 ** (right - left)
                left += 1
        
        return ans % (10 ** 9 + 7)
    
# 时间复杂度O(n log n)，排序。 
# 空间复杂度O(1) 

# 2026.04.07 11:35 

# 灵神的写法 
# 速度有95%以上 
# 最后一定要取模，不取模还是会超出范围。 

# MOD是模 
# MX是题目给的数组最多的元素个数 

# pow2是每个位置存储2的相应次方的数组 
# 索引0处代表2的0次方，因为 2 ** 0 == 1，所以用[i]来初始化数组。 
# 计算下一个次方的结果就用上一个次方乘2再取模。 

# pow2数组要放在 class Solution 之外 

MOD = 1_000_000_007
MX = 100_000 

pow2 = [1] * MX
for i in range(1, MX):
    pow2[i] = pow2[i - 1] * 2 % MOD 

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        ans = 0
        left = 0
        right = len(nums) - 1
        while left <= right: 
            s = nums[left] + nums[right]
            if s > target:
                right -= 1
            else:
                ans += pow2[right - left]
                left += 1
        
        return ans % MOD 
    
# 时间复杂度O(n log n) 
# 空间复杂度O(1) 

# 2026.04.07 11:59 