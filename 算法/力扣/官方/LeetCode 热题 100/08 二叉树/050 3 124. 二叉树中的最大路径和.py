# Definition for a binary tree node.

from cmath import inf
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 2025.12.22 

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf 
        def dfs(node):
            if node is None:
                return 0
            l_val = dfs(node.left)
            r_val = dfs(node.right)
            nonlocal ans 
            ans = max(ans, l_val + r_val + node.val)
            return max(max(l_val, r_val) + node.val, 0)
        dfs(root)
        return ans 
    
# 2026.05.10 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf 

        def dfs(node):
            if node is None:
                return 0 
        
            l_val = dfs(node.left) 
            r_val = dfs(node.right) 
        
            nonlocal ans 
            ans = max(ans, l_val + r_val + node.val) 
        
            return max(max(l_val, r_val) + node.val, 0) 
        
        dfs(root) 
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.05.10 23:02 