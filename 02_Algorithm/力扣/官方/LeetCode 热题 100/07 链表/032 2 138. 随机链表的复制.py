# Definition for a Node.

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# 题解注释 

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 复制每个节点，把新节点直接插到原节点的后面
        cur = head
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next

        # 遍历交错链表中的原链表节点
        cur = head
        while cur:
            if cur.random:
                # 要复制的 random 是 cur.random 的下一个节点
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 删除交错链表中的原链表节点，剩下的节点即为新链表
        cur = dummy = Node(0, head)
        while cur.next:
            # 删除原链表的节点，即当前节点的下一个节点
            # 如果要恢复原链表，见另一份代码【Python3 写法二】
            cur.next = cur.next.next
            cur = cur.next

        return dummy.next
    
# 手敲代码 

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur = head 
        while cur:
            cur.next = Node(cur.val, cur.next)
            cur = cur.next.next 
        
        cur = head 
        while cur:
            if cur.random:
                cur.next.random = cur.random.next 
            cur = cur.next.next 
        
        cur = dummy = Node(0, head) 
        while cur.next:
            cur.next = cur.next.next 
            cur = cur.next 
        return dummy.next 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.27 12:09 
    
# 关键点： 
# 创建dummy和tail的时候其实代表同一个节点，然后tail用来向后遍历，tail改变结构的同时也代表着dummy这个节点之后的结构也发生改变了。 
# 只有dummy这一个哨兵、这个“头头”没有变，后面的其它结构都变了。 
# dummy作为哨兵节点没有改变，dummy.next不断改变了，改变成指向复制后的节点了。 

# 2026.04.27 12:28 