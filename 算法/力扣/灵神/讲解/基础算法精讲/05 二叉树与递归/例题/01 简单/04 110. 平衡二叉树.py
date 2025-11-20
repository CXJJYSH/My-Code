# 第一段是我自己的写法，时间复杂度击败40%以下，空间复杂度击败70%左右。

from typing import Optional

# 单向链表的定义。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    # 用于计算子树的高度。

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True 
        # 判断边界条件，当节点没有左右子树、节点为None时，该节点为根节点的二叉树是平衡的，所以返回True。

        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        # 从根节点还是递归，如果根节点左右子树高度差小于等于一，就继续递归左右子树中的左右子树，判断是否仍为平衡二叉树。

        else: 
            return False 
        # 如果根节点的左右子树高度差就大于一，则可以直接判断这颗二叉树不是平衡二叉树，所以可以直接返回False。 

# 第二段是灵神的方法。实在是太巧妙了，直接通过维护并查看特征值就能判断二叉树是否为平衡二叉树了。 

# 单向链表的定义。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # 在函数作用域内又定义了一个新的函数，新的函数不属于类的管控。

        def get_height(node):
            if node is None:
                return 0
            # 边界条件，节点为空时返回高度0。

            l_depth = get_height(node.left)
            # 递归得到左子树的高度 或 特征值 -1。

            if l_depth == -1:
                return -1
            # 当左子树不是平衡二叉树时，返回特征值-1。否则，正常情况下，最后的return语句正常返回高度值。

            r_depth = get_height(node.right)
            # 递归得到右子树的高度 或 特征值 -1。

            if r_depth == -1 or abs(l_depth - r_depth) > 1:
                return -1
            # 当右子树不是平衡二叉树 或 当前左右子树高度差大于一 时，返回特征值-1。否则，正常情况下，最后的return语句正常返回高度值。

            return max(l_depth, r_depth) + 1
            # 这一句return就实现平衡二叉树情况下高度的正常计算。

        return get_height(root) != -1
        # 最后通过判断get_height(root)结果是否不等于-1判断该二叉树是否为平衡二叉树。
        # 因为 不等于-1，说明是平衡二叉树；等于-1，说明不是平衡二叉树。

# 简单
# 2025.11.20 16:50 