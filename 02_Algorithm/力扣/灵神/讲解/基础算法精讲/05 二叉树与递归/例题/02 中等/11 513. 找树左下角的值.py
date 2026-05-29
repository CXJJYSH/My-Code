from collections import deque
from typing import Optional

# 二叉树定义。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return []
        # 特判空节点。 
        # 题目说了至少有一个节点，所以其实这道题不用特判根节点是否为空。 
        # 直接开始初始化双端队列就好。 
        
        ans = root.val 
        # 把ans = root.val这行删掉也可以。 
        # 因为前面已经特判空节点了，后面若能进入循环,vals.append(node.val)和ans = vals[0]语句的结果就一定是正确的， 
        # 所以就可以将ans放到后面来赋值。

        q = deque([root])
        while q:
            vals = []
            # 遍历每一行的时候先初始化记录数组。

            for _ in range(len(q)):
                # 这里我用了vals数组记录每一行的节点值的话，就一定要再用一层for循环， 
                # 不然就是q每跳出一个节点，vals就置为空数组，去记录下一“个”节点值了，最后返回的会是最后一行最后一个节点的节点值。 
                
                node = q.popleft()
                vals.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # 利用双端队列的便捷特性为记录下一行做准备。

            ans = vals[0]
            # 将ans更新为刚记录的一行的行首节点值。

        return ans 
        # 循环结束后return最新记录的ans，不管有没有都能保证记录的是最后一行行首节点值。 

# 时间复杂度O(n)，每个节点都遍历了一次。
# 空间复杂度O(n)，如果是满二叉树的话队列最多会保存二分之n的节点个数。

# 中等
# 2025.11.28 12:31 从十二点出头开始做的，大概花了半个小时写代码和做笔记。 

# 灵神的代码还是依旧优雅。

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        # 不用特判，直接初始化双端队列。

        while q:
            node = q.popleft()
            
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
            # 调整if语句的判断顺序就能起到调整节点进入双端队列的顺序的效果。

        return node.val 
        # 返回最后记录的node的节点值即可。 

# 灵神的代码在力扣上测试比我快的原因是———— 
# 他代码的常数操作更少，消耗更少的常数时间，即他少了我额外创建数组所消耗的时间， 
# 他的代码常数开销更小，速度略快。 

# 2025.11.28 12:58 