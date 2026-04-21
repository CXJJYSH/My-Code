# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        slow = head 
        fast = head 
        while fast and fast.next: # 只有当快指针非空，且快指针的下一节点非空是才能移动两个指针。 
            slow = slow.next 
            fast = fast.next.next 
        return slow 

    def reverseList(self, head):
        pre = None 
        cur = head 
        while cur: 
            nxt = cur.next 
            cur.next = pre 
            pre = cur 
            cur = nxt 
        return pre 

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middleNode(head)
        head2 = self.reverseList(mid)
        while head2:
            if head.val != head2.val:
                return False 
            head = head.next 
            head2 = head2.next 
        return True 

# 只可能后一段链表更短，所以只判断后链表此时的节点是否为空。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.21 20:33 