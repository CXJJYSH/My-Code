from typing import Optional

# 下面是灵神的题解代码和注释。

class Solution:
    
    # 首先「递」到链表末尾，把末尾节点作为新链表的头节点 rev_head
    # 然后在「归」的过程中，把经过的节点依次插在新链表的末尾（尾插法）
    
    def reverseList(self, head: Optional[Listnode]) -> Optional[ListNode]: # type: ignore
        
        # 判断 head is None 是为了兼容一开始链表就是空的情况
        
        if head is None or head.next is None:
            return head  # 链表末尾，即下面的 rev_head
        rev_head = self.reverseList(head.next)  # 「递」到链表末尾，拿到新链表的头节点
        tail = head.next  # 在「归」的过程中，head.next 就是新链表的末尾
        tail.next = head  # 把 head 插在新链表的末尾
        head.next = None  # 如果不写这行，新链表的末尾两个节点成环，这俩节点互相指向对方
        return rev_head
    
# 下面是我自己写了一遍，然后自己写的注释，感觉自己看懂了之后写的注释更好理解。

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        
        if head is None or head.next is None:
            return head 
        # 这一句要递归到尾节点的时候才会启用。
        
        rev_head = self.reverseList(head.next) 
        # 这一句的作用是得到 当前状态 反转链表 后的 头节点。
        
        tail = head.next 
        # 以最后两个节点举例，可以特化为此时head是倒数第二节点，head.next还是尾节点。
        # 这里将tail赋值为head.next是让尾节点成为 此时 反转后的头节点。
        
        tail.next = head
        # 这里特化是将 尾节点 的下一个节点指向 倒数第二节点。

        head.next = None
        # 这里本来 倒数第二节点 的下一个节点还指向 尾节点，如果不删就有“前指向后，后指向前”的循环节点了。
        # 所以应该将“前指向后”的指向删除，只保留“后指向前”的指向。

        return rev_head
        # 以上的流程覆盖到全体节点就是 从后往前逐步建立链表节点链，每次递归只是建立 当前节点 和 下一节点 之间的指向关系。
        # 当“递”的过程结束之后、“归”的过程归到头节点时，函数执行完成后返回的结果就是整个链表反转后的头节点，所以可以直接返回rev_head。