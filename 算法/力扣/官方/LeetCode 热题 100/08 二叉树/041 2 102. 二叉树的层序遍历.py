# Definition for a binary tree node.

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 两个数组写法 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        ans = []
        
        cur = [root]
        while cur:
            nxt = []
            vals = []
        
            for node in cur:
                vals.append(node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
        
            ans.append(vals)
        
            cur = nxt 
        
        return ans 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.04.30 13:38 

# 一个双端队列写法 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        ans = []

        q = deque([root])

        while q:
            vals = []
            
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(vals)
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.04.30 13:45 