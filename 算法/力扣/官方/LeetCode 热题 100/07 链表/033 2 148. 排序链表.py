# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 题解注释 分治法 

class Solution:
    # 876. 链表的中间结点（快慢指针）
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            pre = slow  # 记录 slow 的前一个节点
            slow = slow.next
            fast = fast.next.next
        pre.next = None  # 断开 slow 的前一个节点和 slow 的连接
        return slow

    # 21. 合并两个有序链表（双指针）
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 用哨兵节点简化代码逻辑
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1  # 把 list1 加到新链表中
                list1 = list1.next
            else:  # 注：相等的情况加哪个节点都是可以的
                cur.next = list2  # 把 list2 加到新链表中
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2  # 拼接剩余链表
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果链表为空或者只有一个节点，无需排序
        if head is None or head.next is None:
            return head
        # 找到中间节点 head2，并断开 head2 与其前一个节点的连接
        # 比如 head=[4,2,1,3]，那么 middleNode 调用结束后 head=[4,2] head2=[1,3]
        head2 = self.middleNode(head)
        # 分治
        head = self.sortList(head)
        head2 = self.sortList(head2)
        # 合并
        return self.mergeTwoLists(head, head2)

# 手敲代码 分治法 

class Solution:
    # 找到中间节点，然后在此将原链表分成两段，用置为None的方法切断前后链表之间的next联系。 
    def middleNode(self, head):
        slow = fast = head 
        while fast and fast.next:
            pre = slow 
            slow = slow.next 
            fast = fast.next.next 
        pre.next = None 
        return slow 
    
    # 合并两个链表。 
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next 
            else:
                cur.next = list2 
                list2 = list2.next 
            cur = cur.next 
        cur.next = list1 if list1 else list2 
        return dummy.next 

    # 进行归并排序。 
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head 
        head2 = self.middleNode(head)
        head = self.sortList(head)
        head2 = self.sortList(head2)
        return self.mergeTwoLists(head, head2) 

# 时间复杂度O(n log n)，递归深度为O(log n)，每一层节点总数为O(n)，总的时间复杂度为两者相乘为O(n log n)。 
# 空间复杂度O(log n)，递归要O(log n)的栈空间。 

# 2026.04.27 12:48 