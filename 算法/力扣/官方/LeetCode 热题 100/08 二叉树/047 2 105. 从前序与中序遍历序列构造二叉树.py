# Definition for a binary tree node.

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 写法一 

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None 
        
        left_size = inorder.index(preorder[0]) # 这里是找出左子树的长度。 
        
        left = self.buildTree(preorder[1 : 1 + left_size], inorder[:left_size])
        right = self.buildTree(preorder[1 + left_size:], inorder[1 + left_size:])
        # 这里是递归构造左子树和右子树。 

        return TreeNode(preorder[0], left, right) # 最后返回构造好的二叉树的根节点。 
    
# 时间复杂度O(n ** 2)，其中 n 为 preorder 的长度。最坏情况下二叉树是一条链，我们需要递归 O(n) 次，每次都需要 O(n) 的时间查找 preorder[0] 和复制数组。 
# 空间复杂度O(n ** 2) 

# 2026.05.07 14:13 

# 写法二 

# 用一个哈希表（或者数组）预处理 inorder 每个元素的下标，这样就可以 O(1) 查到 preorder[0] 在 inorder 的位置，从而 O(1) 知道左子树的大小。 
# 把递归参数改成子数组下标区间（左闭右开区间）的左右端点，从而避免复制数组。 

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {x: i for i, x in enumerate(inorder)} 

        def dfs(pre_l, pre_r, in_l):
            if pre_l == pre_r:
                return None 
            
            left_size = index[preorder[pre_l]] - in_l 
            
            left = dfs(pre_l + 1, pre_l + 1 + left_size, in_l)
            right = dfs(pre_l + 1 + left_size, pre_r, in_l + 1 + left_size)
            
            return TreeNode(preorder[pre_l], left, right)
        
        return dfs(0, len(preorder), 0) 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.05.07 14:37 

# 还有三道相似的拓展题，之后有工夫回来写一下。 

# https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/2646359/tu-jie-cong-on2-dao-onpythonjavacgojsrus-aob8/?envType=study-plan-v2&envId=top-100-liked 

# 2026.05.07 14:41 