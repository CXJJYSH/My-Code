from collections import defaultdict
from typing import List

# 自己写的代码，应该花了2、3分钟 在3分钟以内就完成了，秒杀。 

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        all_set = len(set(nums))
        cnt = defaultdict(int) # 这个用法比Counter()快。灵神在题解里说了。 
        left = 0 
        
        for x in nums:
            cnt[x] += 1
            
            while len(cnt) >= all_set:
                out = nums[left] 
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
                left += 1
            
            ans += left 
        
        return ans 
    
# 这里就用到了 03 2 3325 记下来的知识点，这里要看cnt容器整体，所以要删除键值为0的键。 
    
# 时间复杂度O(n) 
# 空间复杂度O(n)，k为nums中不同元素的个数，不会超过n。 

# 2026.01.31 20:02 

# 灵神的版本，其实算法是完全一样。 

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        ans = 0
        k = len(set(nums))
        cnt = defaultdict(int)
        left = 0

        for x in nums:
            cnt[x] += 1
        
            while len(cnt) == k:
                out = nums[left] 
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out] 
                left += 1
        
            ans += left 
        
        return ans 

# 这一次只用了 01:37 就写完了，所以第一遍应该也挺快的。 

# 时间复杂度O(n) 
# 空间复杂度O(k)，k为nums中不同元素的个数，不会超过n。 

# 2026.01.31 20:11 