from cmath import inf
from typing import Optional

# 二叉树定义 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf 
        # 因为有可能会返回0，所以ans可以初始化为负无穷大。 
         
        def dfs(node):
            if node is None:
                return 0
            # 边界条件返回0。 

            l_val = dfs(node.left)
            r_val = dfs(node.right)
            
            nonlocal ans 
            ans = max(ans, l_val + r_val + node.val)
            # 依旧和543题思路一样，通过递归“拐点”对应的情况更新答案。 
            
            return max(max(l_val, r_val) + node.val, 0)
            # 当前递归返回 当前节点对应的链的节点和最大值 或 0。 

        dfs(root)

        return ans 
    
# 因为每个节点都遍历了一次，每个节点计算答案的时间为O(1)，无额外空间，所以 
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2025.12.22 23:43 