# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetricTree(self, p, q):
        if p is None or q is None:
            return p is q 
        return (p.val == q.val and self.isSymmetricTree(p.left, q.right) and self.isSymmetricTree(p.right, q.left)) 

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricTree(root.left, root.right) 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.04.30 12:45 

# 合成一个函数的写法 

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isSymmetricTree(p, q):
            if p is None or q is None:
                return p is q 
            return (p.val == q.val and 
                    isSymmetricTree(p.left, q.right) and 
                    isSymmetricTree(p.right, q.left)) 
        
        return isSymmetricTree(root.left, root.right) 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.04.30 12:47 