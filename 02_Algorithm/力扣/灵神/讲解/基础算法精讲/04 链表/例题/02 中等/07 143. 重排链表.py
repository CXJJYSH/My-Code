from typing import Optional

# 单向链表定义。

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
        return slow # 返回的都是节点。
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None 
        cur = head 
        while cur:
            nxt = cur.next 
            cur.next = pre
            pre = cur 
            cur = nxt 
        return pre # 返回的都是节点。

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        while head2.next:
            nxt = head.next
            nxt2 = head2.next
            head.next = head2
            head2.next = nxt 
            head = nxt 
            head2 = nxt2 
        # 这道题的难点在于找到重排链表的步骤逻辑，然后运用已经学过的算法知识组合实现这道题要实现的效果。
        # 并且要注意时时更新下一节点变量。
        # 循环条件为while head2.next: ，原因是————
        # 奇数情况下返回唯一的中间节点，偶数情况下返回第二个中间节点，
        # head2初始值是链表的最后一个节点，从右往左循环更新之后必然是head2先到达中间节点（偶数情况下）或head和head2同时到达中间节点（奇数情况下），
        # 当head2到达了中间节点，重排流程到这里就结束了，head2没有下一节点，head2.next为空，
        # 所以循环条件是while head2.next: 。