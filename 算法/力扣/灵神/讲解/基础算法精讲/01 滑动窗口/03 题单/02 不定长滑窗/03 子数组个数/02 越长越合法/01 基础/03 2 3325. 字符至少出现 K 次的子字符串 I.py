from collections import defaultdict

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        ans = 0
        cnt= defaultdict(int)
        left = 0

        for c in s:
            cnt[c] += 1
            
            while cnt[c] >= k:
                cnt[s[left]] -= 1
                left += 1
            
            ans += left 
        
        return ans 
    
# 什么时候需要删值为0的键： 
# 看cnt容器本身时需要删， 
# 看cnt[x]值时不需要删。 

# 这里用 cnt[c] >= k 作为while循环条件可行的原因是，只有上一步 cnt[c] += 1 会触发while循环， 
# 且只有当前c元素键的值达到了k，其它必然小于k、无需判断， 
# 而事实上是cnt[c]刚等于k的时候就触发while循环了，所以while循环条件也可以写为 cnt[c] == k 。 

# 灵神这样写时间复杂度和空间复杂度就很低了。 

# 时间复杂度O(n) 
# 空间复杂度O(U)，U为字符集合的大小。 

# 2026.01.30 14:37 