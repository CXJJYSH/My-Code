# Definition for singly-linked list.

from typing import Optional

# 看完题解手敲 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return head 
        odd_list = head 
        even_list = head.next 
        even_head = even_list 
        while even_list and even_list.next:
            odd_list.next = even_list.next 
            odd_list = odd_list.next 
            even_list.next = odd_list.next 
            even_list = even_list.next 
        odd_list.next = even_head 
        return head 
    
# 题解 

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return head   # 空链表，直接返回
        odd_list = head          # 奇数索引节点链表odd_list初始化为头节点
        even_list = head.next    # 偶数索引节点链表even_list初始化为次节点
        even_head = even_list     # 记录偶数索引节点链表头节点
        
        # 当前偶数节点不为空且当前偶数节点之后还有节点
        while even_list and even_list.next:
            odd_list.next = even_list.next     # 下一个奇数索引节点是当前偶数索引节点的下一个节点
            odd_list = odd_list.next            # 更新当前奇数索引节点
            even_list.next = odd_list.next     # 下一个偶数索引节点是新的奇数索引节点的下一个节点
            even_list = even_list.next          # 更新偶数索引节点
        
        odd_list.next = even_head   # 最后一个奇数索引节点和首个偶数索引节点拼接起来
        return head 
    
# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.27 11:50 