from collections import deque
from typing import Optional

# 二叉树定义。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return []
        ans = root.val 
        q = deque([root])
        while q:
            vals = []
            # 遍历每一行的时候先初始化记录数组。

            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # 利用双端队列的便捷特性为记录下一行做准备。

            ans = vals[0]
            # 将ans更新为刚记录的一行的行首节点值。

        return ans 
        # 循环结束后return最新记录的ans，不管有没有都能保证记录的是最后一行行首节点值。 

# 时间复杂度O(n)，每个节点都遍历了一次。
# 空间复杂度O(n)，如果是满二叉树的话队列最多会保存二分之n的节点个数。

# 中等
# 2025.11.28 12:31 从十二点出头开始做的，大概花了半个小时写代码和做笔记。 