# 单向链表的定义。

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        # 判断特殊情况。

        cur = head 
        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            # 下一节点值重复，则只跳过下一节点，不移动指针。

            else:
                cur = cur.next
            # 下一节点值不重复，则只移动指针。
 
        return head 
        # 因为能够保留初始的头节点，所以可以return head。