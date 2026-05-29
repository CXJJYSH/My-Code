# Definition for a binary tree node.

from collections import defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1

        ans = 0

        def dfs(node, s):
            if node is None:
                return 
            
            nonlocal ans 
            s += node.val 
            ans += cnt[s - targetSum] 

            cnt[s] += 1
            dfs(node.left, s) 
            dfs(node.right, s)
            cnt[s] -= 1

        dfs(root, 0) 

        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 这道题的题解中好多答疑解惑解答得很好，可以随时回看一下。 
# https://leetcode.cn/problems/path-sum-iii/?envType=study-plan-v2&envId=top-100-liked 

# 2026.05.08 11:51 