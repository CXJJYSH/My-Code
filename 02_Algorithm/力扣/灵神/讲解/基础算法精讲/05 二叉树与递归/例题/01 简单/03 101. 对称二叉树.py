from typing import Optional

# 二叉树定义。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def isSymmetricTree(self, p, q):
        # 判断是否是对称树。

        if p is None or q is None:
            return p is q
        # 依旧要检查当前两节点是否为空。

        return (p.val == q.val and self.isSymmetricTree(p.left, q.right) and self.isSymmetricTree(p.right, q.left))
        # 因为是判断是否为对称树，所以要左对右、右对左。

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricTree(root.left, root.right)
        # 最后因为题目保证了至少有一个节点，所以不用判断根节点是否为空，直接对左右子树进行判断是否对称就可以了。 

# 时间复杂度O(n)
# 空间复杂度O(n)

# 简单
# 2025.11.20 15:40