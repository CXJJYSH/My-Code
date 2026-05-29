# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 自顶向下写法 

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def f(node, depth):
            if node is None:
                return 
            
            depth += 1
            
            nonlocal ans 
            ans = max(ans, depth)
            
            f(node.left, depth)
            f(node.right, depth)
        
        f(root, 0)
        
        return ans 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.04.29 12:12 

# 自底向上写法 

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 

        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)

        return max(l_depth, r_depth) + 1 
        # 以最底部节点为例，其左右子节点都为None，都返回0，但该底部节点占用了1深度，所以最后return的时候要加一，才符合数量关系。 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.04.29 12:15 

# 2026.04.29 12:19 