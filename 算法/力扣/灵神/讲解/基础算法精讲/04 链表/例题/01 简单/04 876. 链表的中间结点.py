from typing import Optional

# 单向链表的定义

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head 
        fast = head  
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next  
        return slow 
    
# 这道题主要学习了一下快慢指针的含义和写法————
# 慢指针一次走一节点，快指针一次走两节点，
# 当快指针下一节点为空（奇数情况）或快指针为空（偶数情况）时，停止循环，此时的慢指针就指向应该返回的中间节点。

# 简单
# 2025.11.14 12:15 ~ 12:35 用了大概二十分钟。