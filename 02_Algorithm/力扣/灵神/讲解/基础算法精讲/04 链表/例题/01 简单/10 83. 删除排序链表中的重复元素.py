from typing import Optional

# 单向链表的定义。

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
            # 如果这里不加else: ，则会出现[1, 1, 1, 2, 3]删除不干净的情况，
            # 因为删除第二个1的时候指针就移动到第三个1了，这时候再检查之后的元素是否重复就不能删除之前仍然有重复的元素了。
 
        return head 
        # 因为能够保留初始的头节点，所以可以return head。

# 简单
# 2025.11.18 14:23 大概用了十五分钟