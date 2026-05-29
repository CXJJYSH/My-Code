from typing import Optional

# 二叉树定义。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 下面的灵神方法的代码，优雅，太优雅了。

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q
        # 如果有节点为空，就看是不是都为空。

        return (p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        # 若都不为空，则看节点值是否相等、两节点的左子树是否相等、两节点的右子树是否相等。 

# 时间复杂度O(n)
# 空间复杂度O(n)

# 简单
# 2025.11.20 13:36