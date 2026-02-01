from collections import defaultdict
from typing import List

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        ans = 0
        cnt = defaultdict(int)
        pairs = 0
        left = 0

        for x in nums:
            pairs += cnt[x] 

            cnt[x] += 1 

            while pairs >= k:
                out = nums[left] 
                cnt[out] -= 1

                pairs -= cnt[out] 

                left += 1

            ans += left 

        return ans 
    
# 这道题的奇特之处在于加数对数和减数对数时的数量关系。 
# 进x的时候，进之前有cnt[x]个x，进之后就会增加cnt[x]个数对，所以pairs要先加cnt[x]个，然后再将cnt[x]加1。 
# 出x的时候，出之前有cnt[x]个x，出之后就会减少 cnt[x] - 1 个数对，所以先将当前cnt[x]减1，再将pairs加减1后的cnt[x]个。 

# 这道题一开始看了一下自己不会统计数对数量，之后看了题解之后用时09:58写完了这道题。 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.02.01 20:04 

# 2026.02.01 20:07 