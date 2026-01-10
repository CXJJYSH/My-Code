from cmath import inf
from typing import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        
        '''
        # 看完题解之后自己写一遍就通过了，真爽。
        
        m = len(s) // 4
        cnt = Counter(s)
        if len(cnt) == 4 and min(cnt.values()) == m:
            return 0
        ans = inf
        left = 0
        for right, i in enumerate(s):
            cnt[i] -= 1
            while max(cnt.values()) <= m:
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1
                left += 1
        return ans

        # 这是第一次做这道题的时候的解答。 
        '''

        # 之前做过一遍了，现在再来做一遍还是没思路。 
        # 这道题的方法太独特了，不是靠光套模板能套出来的。 
        
        # 核心是假定一个待替换子串，然后只改这一个子串中的元素，这样子串外的元素就认为是改不了的。 
        # 如果这时候发现待替换子串外的元素中某个元素的个数大于了平衡数，那么怎么改待替换列表，都不能将整个字符串改成平衡字符串。 
        # 所以要想符合条件，就需要待替换子串外的字符每种元素的个数都不要大于平衡树，此时才能保证能替换出平衡字符串，才能进行答案的更新， 

        m = len(s) // 4
        cnt = Counter(s)
        if len(cnt) == 4 and min(cnt.values()) == m:
            return 0 
        
        ans = inf 
        left = 0
        
        for right, x in enumerate(s):
            cnt[x] -= 1
            # 因为是统计待替换子串外的每种元素个数，所以进待替换子串的元素在哈希表中的个数就要减一，因为在待替换子串外的该元素个数减少了一。 
            
            while max(cnt.values()) <= m:
                ans = min(ans, right - left + 1)
                cnt[s[left]] += 1
                # 而此时是弹出待替换子串的操作，所以相应元素在哈希表中表示的个数就要加一。 
                left += 1
        
        return ans 
    
# 时间复杂度O(n * U)，n为s长度，代表外层循环，U为cnt哈希表长度，为内层循环 while max(cnt.values()) <= m: 的时间复杂度， 
# 因为max(cnt.values())中的max()操作会遍历cnt.values()返回的cnt哈希表键值，cnt.values()本身的时间复杂度是O(1)。  

# 空间复杂度O(U)，U为哈希表长度。 

# 2026.01.08 00:31  