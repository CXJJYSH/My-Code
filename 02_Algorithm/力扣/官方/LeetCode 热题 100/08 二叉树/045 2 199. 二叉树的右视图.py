# Definition for a binary tree node.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS 广度优先写法 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        ans = []
        
        cur = [root]
        while cur:
            ans.append(cur[-1].val)
        
            nxt = []
            for node in cur:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
        
            cur = nxt 
        
        return ans 

# 时间复杂度O(n) 
# 空间复杂度O(n)，最后一层。 

# 2026.05.06 12:29 

# DFS 深度优先写法 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node, depth):
            if node is None:
                return 

            if depth == len(ans):
                ans.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)

        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n)，递归深度。 

# 2026.05.06 12:35 