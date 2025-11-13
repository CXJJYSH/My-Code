# 这是看了一遍灵神讲解后自己写出来的代码。

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        # 这是这段代码中单向链表ListNode的定义。
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head 
        while cur:
            n += 1
            cur = cur.next
        # 这一段是用来统计链表的总长度。

        dummy = ListNode(next = head)
        p0 = dummy
        # 这里是初始化虚拟前驱节点和动态前驱节点。
        # dummy不变，p0要更新。

        pre = None 
        cur = p0.next 
        # 这里是初始化pre, cur两个指针。
        # 只用初始化一遍就够了，因为在后续的循环中pre, cur会一直在正确的位置上————即pre指向片段的末尾，cur指向片段的下一个节点。
        # 而p0会指向下一片段的上一节点，p0.next会指向cur。
        # 循环一次之后pre和cur都会在正常的位置上保持前后相邻的顺序。
        # 而片段头节点一开始的错误指向会在p0.next.next中得到正确的修正，所以不用担心for循环刚开始时cur.next有错误指向的问题。

        while n >= k:
            n -= k 
            for _ in range(k):
                nxt = cur.next 
                cur.next = pre 
                pre = cur 
                cur = nxt
            # 这个for循环是让片段链表反转。
             
            nxt = p0.next 
            p0.next.next = cur 
            p0.next = pre 
            p0 = nxt
            # 这一段是正确修改片段反转后与原链表的连接关系。
            # 这里要明确片段链表反转后，下一链表的上一节点是哪个节点。这里其实就是未修改时p0的下一个节点p0.next,即反转片段的原头节点。
            # 要用nxt把p0.next先保存下来。
            # 上面也用了nxt，但是nxt在上面已经起完作用了，所以这里给nxt赋新的值没有问题。
            # 最后nxt也会正确利用。
            
        return dummy.next 
        # 最后返回虚拟前驱节点的下一个节点即可，dummy.next就是整段链表的头节点。

# 困难
# 2025.11.13 10:55 ~ 11:45 花了大概五十分钟。