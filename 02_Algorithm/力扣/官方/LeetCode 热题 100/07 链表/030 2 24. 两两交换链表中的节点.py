# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node0 = dummy = ListNode(next = head)
        node1 = head 
        
        while node1 and node1.next:
            node2 = node1.next 
            node3 = node2.next 

            node0.next = node2
            node2.next = node1 
            node1.next = node3 

            node0 = node1 
            node1 = node3 
        
        return dummy.next 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.23 10:49 