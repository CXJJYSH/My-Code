from typing import Counter, List

class Solution:
    def beautifulBouquet(self, flowers: List[int], cnt: int) -> int:
        ans = 0
        num = Counter()
        left = 0
        
        for right, x in enumerate(flowers):
            num[x] += 1
            
            while num[x] > cnt:
                out = flowers[left]
                num[out] -= 1
                if num[out] == 0:
                    del num[out]
                left += 1
            
            ans += right - left + 1
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.01.26 23:18 

# Counter()和defaultdict()的区别： 
# Counter()专门用来计数，默认值是数字0；（数次数） 
# defaultdict()是通用容器，默认值可自己设置，可以用来存储不同的结构。（存结构） 
# Counter()的专用方法多，defaultdict()几乎没有。 

# 2026.01.26 23:28 