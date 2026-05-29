from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}

        ans = []

        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])

            if end == i:
                ans.append(end - start + 1)
                start = end + 1

        return ans 
    
# 看完代码感觉挺简单的，一下就理解题解了，还是代码简洁。 

# 时间复杂度O(n) 
# 空间复杂度O(U)，U为字符集合大小。 

# 2026.05.26 11:50 