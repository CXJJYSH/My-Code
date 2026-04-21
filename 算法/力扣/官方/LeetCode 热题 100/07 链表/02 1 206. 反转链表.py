# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

# 迭代 头插法 

# 很好理解 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next 
            cur.next = pre 
            pre = cur
            cur = nxt 
        return pre
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.21 20:12 

# 递归 尾插法 

# 一点都不好理解，MD。 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head 
        rev_head = self.reverseList(head.next) 
        tail = head.next 
        tail.next = head 
        head.next = None 
        return rev_head 
    
# 时间复杂度O(n) 
# 空间复杂度O(n) 

# 2026.04.21 20:14 