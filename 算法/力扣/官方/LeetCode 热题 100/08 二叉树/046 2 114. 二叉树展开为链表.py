# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 头插法 

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

# 分治 

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None 
        
        left_tail = self.flatten(root.left)
        right_tail = self.flatten(root.right) 
        
        if left_tail:
            left_tail.right = root.right 
            root.right = root.left 
            root.left = None 
        
        return right_tail or left_tail or root 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.05.07 13:21 