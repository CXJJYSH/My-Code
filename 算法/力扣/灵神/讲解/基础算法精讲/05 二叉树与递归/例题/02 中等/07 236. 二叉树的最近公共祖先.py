class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # 被灵神虐爆了。
        # 灵神的代码太优雅了。
        
        if root is None or root is p or root is q:
            return root
        # 节点为空或目标节点时返回当前节点。
 
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # left和right两个变量的值要么是空节点要么是节点值。

        if left and right:
            return root
        # 目标节点在当前节点的左子树和右子树中，返回当前节点。
         
        if left: 
            return left
        # 如果只在左子树中，就返回左子树递归的结果。
 
        return right 
        # 如果前面的条件都不满足，则为“在右子树中”或“左右子树中都不存在”的情况，此时只要返回对右子树递归的结果就能涵盖两种情况。

# 时空复杂度都是O(n)
# 中等
# 2025.11.26 23:05 ~ 23:20 花了十五分钟。