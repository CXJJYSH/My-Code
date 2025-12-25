from cmath import inf
from typing import Optional

# 二叉树定义 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return inf, 0, 0
            # 边界条件

            l_choose, l_by_fa, l_by_children = dfs(node.left)
            r_choose, r_by_fa, r_by_children = dfs(node.right)
            # 先进行递归拿到这一层递归需要用到的数据。 
            
            choose = min(l_choose, l_by_fa, l_by_children) + min(r_choose, r_by_fa, r_by_children) + 1
            by_fa = min(l_choose, l_by_children) + min(r_choose, r_by_children) 
            by_children = min(l_choose + r_by_children, l_by_children + r_choose, l_choose + r_choose) 
            # 然后对当前节点是否安装摄像头进行分类讨论，其中一种安装的情况，两种不安装的情况。 
            # 具体分为：安装；不安装，被父节点监控；不安装，被子节点监控。 
            # 再用状态转移公式计算出当前递归需要返回的值。 

            return choose, by_fa, by_children 
        
        choose, _, by_children = dfs(root)
        # 因为根节点没有父节点，所以从根节点开始递归的时候可以不关心by_fa状态的值是多少，只关心另外两个状态就好。 

        return min(choose, by_children) 
        # 最后 返回关心的两个状态的最小值就好。 

# 因为每个节点都遍历了一遍，计算时间为O(1)，所以 
# 时间复杂度O(n) 
# 因为最坏情况下，二叉树只有一边的节点，退化成链表，递归要使用O(n)的栈空间，所以 
# 空间复杂度O(n) 

# 2025.12.24 17:15 

# 变形 一 

# 在节点x安装摄像头需要花费cost[x]的费用，求监控所有节点的最小花费。 

# 只需要把choose = min(l_choose, l_by_fa, l_by_children) + min(r_choose, r_by_fa, r_by_children) + 1中的+1改成+cost[node]就好了。 

# 2025.12.24 17:19 

# 变形 二 

# 如果一个红色节点有多个子节点呢？ 

# 之前计算方法在红色节点子节点多的情况下红色情况的计算公式就很复杂，需要简化计算方法。 

# 因为只用考虑子节点是蓝色还是红色的情况，而至少有一个蓝色就行了，所以可以逐个节点取蓝色和红色的最小值， 
# 然后再用每个节点的蓝红结果差值取最小值后与0比较，如果最小值>=0，说明所有蓝色情况所用摄像头都更多，本应该全部都选红色， 
# 但是至少需要有一个蓝色节点，所以要将差值最小的情况的红色改成蓝色，这样才能符合题目要求， 
# 公式写法为+ max(0, 最小值)。 
# 公式前半部分与黄色情况的计算公式完全一样。 

# 这道题其实就是洛谷 P2458 保安站岗问题。 

# 2025.12.24 17:39 