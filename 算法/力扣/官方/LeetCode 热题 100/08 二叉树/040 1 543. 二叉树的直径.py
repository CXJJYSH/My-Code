# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 第一种写法 

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            if node is None:
                return -1 
            l_len = dfs(node.left) + 1
            r_len = dfs(node.right) + 1
            nonlocal ans 
            ans = max(ans, l_len + r_len) 
            return max(l_len, r_len) 
        
        dfs(root) 
        
        return ans 
    
# 第二种写法 

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            if node is None:
                return 0 
            l_len = dfs(node.left) 
            r_len = dfs(node.right)
            nonlocal ans 
            ans = max(ans, l_len + r_len) 
            return max(l_len, r_len) + 1
        
        dfs(root) 

        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.04.30 13:15 

# 在评论区找到一个更好理解什么时候要加一的解释了。 

# 20026.04.30 13:20 