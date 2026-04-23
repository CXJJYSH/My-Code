# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        right = dummy
        for _ in range(n):
            right = right.next 
        left = dummy 
        while right.next:
            left = left.next 
            right = right.next 
        left.next = left.next.next 
        return dummy.next 

# 上面是2025.11.17 的版本。 

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = dummy = ListNode(next = head)
        for _ in range(n):
            right = right.next 
        while right.next:
            left = left.next 
            right = right.next 
        left.next = left.next.next 
        return dummy.next 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.23 10:42 