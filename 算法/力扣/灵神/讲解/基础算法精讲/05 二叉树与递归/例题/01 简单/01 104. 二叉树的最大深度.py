# 这段视频讲解，灵神首次讲了递归的原理，并演示了一遍递归是如何工作的。
# 当能抽象出子问题和原问题时，就可以使用递归。

# 方法一：直接返回结果，不维护外部变量。

from typing import Optional

# 单向链表的定义。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # 特判节点为空的情况。

        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)
        # 分别递归左右子树。

        return max(l_depth, r_depth) + 1
        # 最后返回左右子树最大长度加一。

# 时间复杂度O(n)
# 空间复杂度O(n)，因为用到了栈。

# 方法二：维护一个记录最大节点个数的外部变量。

from typing import Optional

# 单向链表的定义。

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left 
        self.right =right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        def f(node, cnt):
            if node is None:
                return 
            # 特判节点为空的情况。

            cnt += 1
            nonlocal ans 
            ans = max(ans, cnt)
            # 进入当前节点就更新当前最大节点值。

            f(node.left, cnt)
            f(node.right, cnt)
        f(root, 0)
        return ans 
    
# 时间复杂度O(n)
# 空间复杂度O(n)，因为用到了栈。

# 简单
# 2025.11.19 15:45 花了大概半个小时，可能更多一点。 