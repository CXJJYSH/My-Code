from cmath import inf
from typing import Optional

# 二叉树定义。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def isValidBST(self, root: Optional[TreeNode], left = -inf, right = inf) -> bool:
        # 前序遍历
        # 先判断，再递归
        # 时空复杂度都是O(n)
        
        if root is None:
            return True 
        
        x = root.val 
        
        return left < x < right and self.isValidBST(root.left, left, x) and self.isValidBST(root.right, x, right)
    
class Solution2:
    
    pre = -inf 
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 中序遍历
        # 大于上一个节点
        # 时空复杂度都是O(n)
        
        if root is None:
            return True 
        if not self.isValidBST(root.left):
            return False 
        # 判断左子树是否为有效二叉搜索树。

        if root.val <= self.pre:
            return False 
        # 如果不符合中序遍历应得到的节点规律就返回False。

        self.pre = root.val 
        # 更新self.pre为当前节点值。

        return self. isValidBST(root.right)
        # 然后，也是最后，递归右子树，判断右子树是否为有效二叉搜索树。

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 后序遍历
        # 先递归，再判断
        # 时空复杂度都是O(n)

        def f(node):
            if node is None:
                return inf, -inf # 空集，我的理解是用空集表示空节点能让空节点对其它节点没有影响。
            
            l_min, l_max = f(node.left)
            r_min, r_max = f(node.right)
            
            x = node.val 
            
            if x <= l_max or x >= r_min:
                return -inf, inf # 全集，我的理解是用全集表示不符合条件的情况就是直接认定整颗二叉树不是二叉搜索树。
            
            # 至于空集、全集的返回结果为什么要这样表示，以及这样表示巧妙的逻辑，我目前只能绞尽脑汁从头到尾理解一遍，
            # 这个技巧我现在只处于能记住、但不能灵活根据情况选用的阶段。
            # 之后再看看有没有机会更深地理解这个技巧吧。
            
            return min(l_min, x), max(x, r_max)
            # 这里要把x加进来比较的原因是————
            # 如果node是其父节点的右节点，那么返回以node为根节点的树的范围时，也要把node节点的值考虑进去比较，不然可能会漏掉右子树的最小值，
            # 如果node是其父节点的左节点，那么返回以node为根节点的树的范围时，也要把node节点的值考虑进去比较，不然可能会漏掉左子树的最大值，
            # 如果不加进去比较，可能会使非二叉搜索树的二叉树被判断为二叉搜索树，
            # 所以要把x加进来比较。
        return f(root)[1] != inf 
    
# 中等
# 2025.11.25 17:51 花了两个小时多一点的时间消化了一遍这题的三种遍历方法。 