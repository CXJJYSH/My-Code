# 下面这段代码是灵神的方法。

from typing import Optional

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(next = head)
        # 建立一个虚拟前驱节点，使其始终指向头节点。

        p0 = dummy 
        # 创建变量p0，使p0的值等于虚拟前驱节点，方便之后对片段链表的反转。

        for _ in range(left - 1):
            p0 = p0.next 
        # range(n)就是循环执行n次。
        # 这里执行left - 1次就能使p0到达第left节点的上一个节点
        # 这里还要明确的点是left和right并不是像列表索引一样的东西，这里的left就代表第left个，right就代表第right个，比如left = 1意味着left代表第1个。
        # 通过不断使当前节点等于当前节点的下一节点实现片段链表前一节点的索引。

        pre = None
        cur = p0.next 
        for _ in range(right - left + 1):
            nxt = cur.next 
            cur.next = pre 
            pre = cur 
            cur = nxt 
        # 这一段是像整段链表反转一样，对片段链表进行反转，方法是一样的，确定好pre和cur之后修改指向即可。
        # 片段链表一共有(right - left + 1)个元素，结合pre和cur的位置性质可知需要执行(right - left + 1)次，所以使用range(right - left + 1)。

        p0.next.next = cur 
        p0.next = pre 
        # 循环结束后，pre指向原片段尾节点，cur指向原片段尾节点的下一节点。
        # 这里是p0本来指向片段链表的上一个节点，p0的下一节点本来是指向片段链表的头节点。
        # 而现在要将片段链表反转，指向关系就变为原片段的上一节点p0应指向片段链表的原尾节点，片段链表内部指向关系由上一段循环代码实现。
        # 而片段链表的原头节点的下一个节点应该指向原片段的下一节点。
        # 所以第一行的意思是“原片段的头节点的下一节点指向原片段的下一节点”，
        # 第二行的意思是“原片段的上一节点指向原片段的尾节点”。
        
        return dummy.next 
        # 不能return head，只能return dummy.next。
        # 因为根据实际运行结果来看head仍然会指向最先的头节点，若整个链表的头节点已经改变，head不会跟着变化。
        # 而dummy.next因为dummy = ListNode(next = head)所以能够跟着整体头节点的变化而变化，从而始终指向正确的头节点。
        # 所以最后只能返回dummy.next，不能返回head。

# 中等
# 2025.11.12 16:19
# 花了大概一小时，从15:20左右写到16:20。