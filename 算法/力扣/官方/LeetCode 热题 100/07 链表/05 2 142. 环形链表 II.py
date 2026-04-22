# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head 
        fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if fast is slow:
                while slow is not head:
                    slow = slow.next 
                    head = head.next 
                return slow 
        return None 

# 可以数学证明从相遇时开始头节点和慢指针同步移动能相遇在入环点。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.22 14:25 