# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        
        carry = 0
        
        while l1 or l2 or carry: # 每一个节点都是保存的当前carry值模10的余数，所以l1和l2有节点的话就要记录，carry不为0的话也要记录。 
            if l1:
                carry += l1.val
                l1 = l1.next 
            if l2:
                carry += l2.val
                l2 = l2.next
            # 到这为止carry的值就是当前正确的值了。 
            # 然后再进行其它操作。 

            cur.next = ListNode(carry % 10)
            carry //= 10
            cur = cur.next 
            # 指针都要不断移动。 
        
        return dummy.next 
    
# 时间复杂度O(n)，n为l1和l2两者长度的最大值。 
# 空间复杂度O(1) 

# 2026.04.22 15:01 