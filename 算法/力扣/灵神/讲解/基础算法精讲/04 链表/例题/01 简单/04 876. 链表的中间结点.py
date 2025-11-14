from typing import Optional

# 单向链表的定义

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head 
        fast = head  
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next  
        return slow 
    
# 这道题主要学习了一下快慢指针的含义和写法————
# 慢指针一次走一节点，快指针一次走两节点，
# 当快指针下一节点为空（奇数情况）或快指针为空（偶数情况）时，停止循环，此时的慢指针就指向应该返回的中间节点。

# 简单
# 2025.11.14 12:15 ~ 12:35 用了大概二十分钟。

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        A = [head]
        # 创建一个保存链表节点的列表。

        while A[-1].next: # 当列表最后一个元素的下一节点不为空时，继续循环。
            A.append(A[-1].next) # 将非空节点加入列表。
        # 每次加入非空节点后，列表A的最后节点都变为最新加入的节点，所以可以实现向后遍历。

        return A[len(A) // 2]
        # 最后用索引返回列表的元素。
        # 因为使用的是索引，所以奇数情况整除的结果刚好是中间节点的索引，偶数情况整除的结果刚好是第二个中间节点的索引。
        # 奇数情况可以用[1, 2, 3, 4, 5]举例：5 // 2 = 2，指向中间节点3。
        # 偶数情况可以用[1, 2, 3, 4, 5, 6]举例：6 // 2 = 3， 指向第二个中间节点4。
        # 所以这种方法也可行。
    
# 这一段是2025.05.07 21:25提交的，用的应该是逐个遍历，然后返回保存的列表的中间元素。（没错，就是这样的方法。）
# 我感觉这个方法不如灵神的方法优雅，而且适用性没那么强。
# 2025.05.07 21:25 提交
# 2025.11.14 12:42 记
# 2025.11.14 12:51 记完