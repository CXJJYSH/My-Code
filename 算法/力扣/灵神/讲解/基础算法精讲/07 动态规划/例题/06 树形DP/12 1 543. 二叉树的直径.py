from typing import Optional

# 二叉树的定义。 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            if node is None:
                return -1 # 这样设置边界条件就能使之后两个取max的地方边界情况都有正确的结果0。 
            
            l_len = dfs(node.left)
            r_len = dfs(node.right)
            
            nonlocal ans 
            ans = max(ans, l_len + r_len + 2)
            
            return max(l_len, r_len) + 1
        
        dfs(root) 
        
        return ans 
    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(node):
            if node is None:
                return -1
            
            l_len = dfs(node.left) + 1
            r_len = dfs(node.right) + 1
            # 这里也可以都在末尾加一，意思是加上当前节点分别连着左右子树的两条链。 
            
            nonlocal ans 
            ans = max(ans, l_len + r_len)
            
            return max(l_len, r_len)
        
        dfs(root) 
        
        return ans 
    
# 因为遍历了一遍所有节点，每个节点计算结果的时间是O(1)，所以 
# 时间复杂度O(n) 
# 因为最坏情况下这棵二叉树是一条链，递归需要O(n)的栈空间，所以 
# 空间复杂度O(n) 

# 2025.12.20 14:13 