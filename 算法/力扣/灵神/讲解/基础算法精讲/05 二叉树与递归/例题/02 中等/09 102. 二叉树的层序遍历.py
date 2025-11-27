from typing import List, Optional

# 二叉树定义。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        # 这里不能省略。
        # 如果省略了，当cur = [None]时，会将cur判断为一个非空列表，while cur: 会进入循环，导致node is None，在调用node.val、node.left、node.right时会出错。
        
        ans = []
        cur =[root]
        
        while cur:
            vals = []
            nxt = []
            
            for node in cur:
                vals.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            
            ans.append(vals)
            cur = nxt

        return ans
        # 至于为何要有一个vals列表，而不是直接将node.val加入到ans中，
        # 原因是题目要返回[ [3], [9,20], [15,7] ]这种形式的列表，
        # 如果直接加入到ans里，就会返回[ 3, 9, 20, 15, 7 ]这样的列表，与题目要求不符。 

# 时间复杂度O(n)，因为是循环，而整个循环每个节点只遍历了一次，所以时间复杂度为O(n)。
# 空间复杂度也是O(n)，因为二叉树为满二叉树时，循环到倒数第二层，nxt里会有最后一层的二分之n个节点，因此空间复杂度为O(n)。

# 中等
# 2025.11.27 15:30 看起来花的时间比较久是因为中间干别的事去了（试了一下新的加速器，biubiu加速器）。 