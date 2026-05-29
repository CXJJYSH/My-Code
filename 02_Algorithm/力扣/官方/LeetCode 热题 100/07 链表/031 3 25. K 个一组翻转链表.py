# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head 
        while cur:
            n += 1
            cur = cur.next

        dummy = ListNode(next = head)
        p0 = dummy

        pre = None 
        cur = p0.next 

        while n >= k:
            n -= k 
            for _ in range(k):
                nxt = cur.next 
                cur.next = pre 
                pre = cur 
                cur = nxt 
            nxt = p0.next 
            p0.next.next = cur 
            p0.next = pre 
            p0 = nxt 
        return dummy.next 

# 上面是2025.11.13的版本。 

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head 
        while cur:
            n += 1
            cur = cur.next 

        p0 = dummy = ListNode(next = head)
        
        pre = None 
        cur = head # 反转一段结束时pre和cur的位置性质要联系灵神讲的规律来记，写代码时也有应用。 
        while n >= k:
            n -= k 
            
            for _ in range(k): # cur从头到尾一共k个元素，反转操作要循环k次。 
                nxt = cur.next 
                cur.next = pre
                pre = cur  
                cur = nxt # 这里是反转长度为k的片段。 

            nxt = p0.next 
            p0.next.next = cur # 这里我感觉写成 nxt.next = cur 可读性更好。 
            p0.next = pre 
            p0 = nxt 
            # 这里是将哨兵连接到反转后的头节点，以及将反转后的尾节点连接到未反转的下一段的开头。 
            # 然后再将哨兵放到下一段的前一个节点，用nxt才不会交换错。 

        return dummy.next 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.23 11:38 