from collections import deque
from typing import List, Optional

# 二叉树定义。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        q = deque([root]) # 用双端队列写。
        even = False
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(vals[::-1] if even else vals)
            even = not even 
        return ans 
        # 也可以用两个cur, nxt数组来写。 

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        ans = []
        cur = [root]
        even = False 
        while cur:
            nxt = []
            vals = []
            for node in cur:
                vals.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            ans.append(vals[::-1] if even else vals)
            cur = nxt 
            even = not even 
        return ans 
    
# 时间复杂度O(n)
# 空间复杂度O(n)
# 2025.11.27 23:42 