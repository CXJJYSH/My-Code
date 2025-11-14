from typing import Optional

# 下面是单向链表的定义。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            if fast is slow: # if slow == fast: 也可以，但是在力扣上运行的时间复杂度相差很大。is 是88.23%，== 是43.13%。
                return True
        return False