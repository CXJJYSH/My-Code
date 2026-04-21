# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p = headA 
        q = headB 
        while p is not q:
            p = p.next if p else headB # 默认单向链表的最后一个节点为空节点，单向链表以空节点结束。非空节点的下一个节点可以为空。 
            q = q.next if q else headA 
        return p 
    
# 时间复杂度O(m + n) 
# 空间复杂度O(1) 

# 2026.04.21 19:39