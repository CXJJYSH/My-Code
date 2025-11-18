from typing import Optional

# 单向链表的定义。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        # 这里头节点可能会被删除，所以应该创建一个dummy哨兵节点。

        cur = dummy 
        # 初始化指针指向dummy节点。

        while cur.next and cur.next.next: 
            # cur之后还有两个节点时继续循环。
            
            val = cur.next.val
            # 让cur之后的第一个节点的值作为检查量。
             
            if cur.next.next.val == val:
                # 当cur后两个节点值重复时：

                while cur.next and cur.next.val == val:
                    # cur下一节点存在且值和之前的节点值重复。

                    cur.next = cur.next.next
                    # 删除重复的节点。
                 
            else:
                # 当cur后两个节点值不重复时：

                cur = cur.next
                # 将指针移动至下一节点。
                 
        return dummy.next 
        # 最后使用哨兵节点的性质正确返回头节点。

# 中等
# 2025.11.18 14:51 用了大概二十五分钟。关键是灵神讲得好。
# 自己一开始也想了一遍，但是没想出有效的方法来，最后还是看了灵神的讲解再写了一遍。