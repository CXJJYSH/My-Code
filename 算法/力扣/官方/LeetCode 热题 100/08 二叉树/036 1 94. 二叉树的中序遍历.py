# Definition for a binary tree node.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 前序遍历：根-左-右。先获取根节点值，再访问根的左子树，最后访问根的右子树。 
# 中序遍历：左-根-右。先访问根的左子树，再获取根节点值，最后访问根的右子树。 
# 后序遍历：左-右-根。先访问根的左子树，再访问根的右子树，最后获取根节点值。 

# 这下二叉树的前序、中序、后序遍历我都会了。 

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node):
            if node is None:
                return 
            dfs(node.left) 
            ans.append(node.val)
            dfs(node.right)
        ans = []
        dfs(root)
        return ans 
    
# 时间复杂度O(n)，n为二叉树节点个数。 
# 空间复杂度O(h)，h为二叉树的高度，递归需要O(n)的栈空间。  

# 2026.04.28 16:21 

# 明天看O(1)空间复杂度的写法。 

# 2026.04.28 16:25 