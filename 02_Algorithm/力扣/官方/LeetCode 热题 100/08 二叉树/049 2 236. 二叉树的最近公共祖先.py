# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 2025.11.26 的提交 

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 被灵神虐爆了。

        if root is None or root is p or root is q:
            return root 

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root 

        if left: 
            return left 

        return right 
    
# 2026.05.08 11:53 

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None, p, q):
            return root 
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self. lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root 
        
        return left or right 
    
# 太简洁了，好神奇 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.05.08 11:58 