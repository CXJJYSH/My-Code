# 这道题是要删除链表倒数第 n 个节点。

# 单向链表的定义。

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val

        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(next = head)
        # 先确保能够正确找到头节点。

        right = dummy
        for _ in range(n):
            right = right.next 
        # 然后先让right向右走n步。

        left = dummy 
        while right.next:
            left = left.next 
            right = right.next 
        # 再让left和right一起走，知到right指向最后一个节点。
        # 此时left就指向倒数第n + 1个节点，刚好是要删除节点的前一个节点。

        left.next = left.next.next 
        # 然后让倒数第n + 1个节点的指向跳过倒数第n个节点，即跳过要删除的节点，即可达到删除节点的效果。

        return dummy.next 
        # 最后用dummy.next返回正确的头节点即可。 