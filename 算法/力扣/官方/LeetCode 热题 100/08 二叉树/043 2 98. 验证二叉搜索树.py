# Definition for a binary tree node.

from cmath import inf
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 后序遍历写法 

# 还有前序遍历和后序遍历的写法 

# 这道题好难，我不知道怎么规定判定条件 

# TMD，每天写一道题就走吧，要是又简单题就可以多做几道简单题，先把JS搞完来。 

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return inf, -inf 
            
            l_min, l_max = dfs(node.left)
            r_min, r_max = dfs(node.right)
            
            x = node.val 
            if x <= l_max or x >= r_min:
                return -inf, inf 
            
            return min(l_min, x), max(r_max, x) 
        
        return dfs(root)[1] != inf 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.05.05 22:18 