# 二叉树定义。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        x = root.val 
        # 取当前节点值，用于之后的比较来判断属于哪种情况。
        
        if p.val < x and q.val < x:
            return self.lowestCommonAncestor(root.left, p, q)
        # 都在左子树中，递归左子树。

        if p.val > x and q.val > x:
            return self.lowestCommonAncestor(root.right, p, q)
        # 都在右子树中，递归右子树。

        return root 
        # 各在左右子树中，或当前节点为目标节点之一，返回当前节点。