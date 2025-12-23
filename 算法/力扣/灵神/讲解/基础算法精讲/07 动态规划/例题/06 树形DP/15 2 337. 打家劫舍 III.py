from typing import Optional

# 二叉树定义 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return 0, 0
            
            l_rob, l_not_rob = dfs(node.left)
            r_rob, r_not_rob = dfs(node.right)
            # 左子节点和右子节点选与不选的状态结果由进一步的递归返回。 
            
            rob = l_not_rob + r_not_rob + node.val 
            not_rob = max(l_rob, l_not_rob) + max(r_rob, r_not_rob)
            # 这里保存当前节点选与不选的状态结果，然后在最后进行返回。 

            return rob, not_rob 
        
        return max(dfs(root)) 
        # 因为递归函数返回的结果包含两个不同情况下的值，这里取最大值即可得到正确答案。 

# 因为每个节点只递归了一次，计算结果需要的时间是O(1)，所以 
# 时间复杂度O(n) 
# 因为最坏情况下，这颗二叉树是一条链，递归需要O(n)的栈空间，所以 
# 空间复杂度O(n) 

# 2025.12.23 17:06 