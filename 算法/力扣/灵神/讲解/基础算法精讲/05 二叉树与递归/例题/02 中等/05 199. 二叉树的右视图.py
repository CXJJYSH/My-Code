from typing import List, Optional

# 单向链表定义。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 这道题灵神的方法和我猜测的后序遍历方法不一样，他使用了一种我没预想到、之前也没见过的方法。
        # 所以这道题还是偶尔搭配视频使用更合适。
        
        ans = [] 
        def f(node, depth):
            if node is None:
                return 
            # 如果节点为空就直接返回。

            if depth == len(ans):
                ans.append(node.val)
            # 根节点深度为0。
            # 如果当前深度等于答案列表长度，则将当前节点值计入到答案列表中。

            f(node.right, depth + 1)
            # 要找右视图，
            # 所以先递归右子树，右子树有节点要记的话很多情况下就没有左子树节点的事了。

            f(node.left, depth + 1)
            # 再递归左子树。

        f(root, 0)
        # 最后对题目所给树执行刚刚编写的函数。

        return ans 
        # 最后返回答案列表即可。

# 时空复杂度都是O(n)。

# 中等
# 2025.11.24 13:48 花了大概半小时左右。