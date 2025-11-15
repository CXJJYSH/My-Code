from typing import Optional

# 下面是单向链表的定义。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head 
        fast = head 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

            if fast is slow:
                while slow is not head:
                    slow = slow.next 
                    head = head.next 
                    # 这里有结论————快慢指针相遇后，慢指针继续走到入口时，head以同样的速度走到的位置距离入口正好是环长的倍数。
                    # 所以继续一步一步走能在有环的情况下在入口相遇。
                    # 数学推导在幕布笔记和灵神视频讲解里。
                    # 幕布笔记 https://mubu.com/app/edit/recent/3Oqp73YCBw3#4ZCbW7dV99 
                    # 灵神讲解 https://www.bilibili.com/video/BV1KG4y1G7cu/?vd_source=72e41d7969e9dc71609c47e6fe7c343e&spm_id_from=333.788.videopod.sections 
                return slow 
                # 有环的话返回slow或head任意一个即可。

        return None # 没有的话返回None。