# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 记录答案的写法 

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0

        def dfs(node):
            nonlocal k, ans 
        
            if node is None or k <= 0:
                return 
        
            dfs(node.left)
        
            k -= 1
            if k == 0:
                ans = node.val 
        
            dfs(node.right)
        
        dfs(root)
        
        return ans 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.05.06 11:52 

# 不记录答案的写法 

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(node):
            if node is None:
                return -1 

            left_res = dfs(node.left)
            if left_res != -1:
                return left_res 

            nonlocal k 
            k -= 1
            if k == 0:
                return node.val 

            return dfs(node.right) 

        return dfs(root) 

# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.05.06 12:00 