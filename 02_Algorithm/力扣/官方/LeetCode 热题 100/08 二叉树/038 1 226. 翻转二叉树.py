# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 写法一 递归到底部再交换 

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None 
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        root.left = right 
        root.right = left 
        
        return root 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.04.29 12:27 

# 写法二 先顶部交换再递归 

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None 

        root.left, root.right = root.right, root.left 

        self.invertTree(root.left)
        self.invertTree(root.right) 

        return root 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.04.29 12:31 