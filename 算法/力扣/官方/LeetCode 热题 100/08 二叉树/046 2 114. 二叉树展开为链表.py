# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    head = None 
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return  
        
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.left = None 
        root.right = self.head 
        
        self.head = root 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.05.07 13:14 