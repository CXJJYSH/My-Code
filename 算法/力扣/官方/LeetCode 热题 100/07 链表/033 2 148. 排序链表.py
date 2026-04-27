# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 题解注释 分治法 

class Solution:
    # 876. 链表的中间结点（快慢指针）
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            pre = slow  # 记录 slow 的前一个节点
            slow = slow.next
            fast = fast.next.next
        pre.next = None  # 断开 slow 的前一个节点和 slow 的连接
        return slow

    # 21. 合并两个有序链表（双指针）
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 用哨兵节点简化代码逻辑
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1  # 把 list1 加到新链表中
                list1 = list1.next
            else:  # 注：相等的情况加哪个节点都是可以的
                cur.next = list2  # 把 list2 加到新链表中
                list2 = list2.next
            cur = cur.next
        cur.next = list1 if list1 else list2  # 拼接剩余链表
        return dummy.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 如果链表为空或者只有一个节点，无需排序
        if head is None or head.next is None:
            return head
        # 找到中间节点 head2，并断开 head2 与其前一个节点的连接
        # 比如 head=[4,2,1,3]，那么 middleNode 调用结束后 head=[4,2] head2=[1,3]
        head2 = self.middleNode(head)
        # 分治
        head = self.sortList(head)
        head2 = self.sortList(head2)
        # 合并
        return self.mergeTwoLists(head, head2)

# 手敲代码 分治法 

class Solution:
    # 找到中间节点，然后在此将原链表分成两段，用置为None的方法切断前后链表之间的next联系。 
    def middleNode(self, head):
        slow = fast = head 
        while fast and fast.next:
            pre = slow 
            slow = slow.next 
            fast = fast.next.next 
        pre.next = None 
        return slow 
    
    # 合并两个链表。 
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next 
            else:
                cur.next = list2 
                list2 = list2.next 
            cur = cur.next 
        cur.next = list1 if list1 else list2 
        return dummy.next 

    # 进行归并排序。 
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head 
        head2 = self.middleNode(head)
        head = self.sortList(head)
        head2 = self.sortList(head2)
        return self.mergeTwoLists(head, head2) 

# 时间复杂度O(n log n)，递归深度为O(log n)，每一层节点总数为O(n)，总的时间复杂度为两者相乘为O(n log n)。 
# 空间复杂度O(log n)，递归要O(log n)的栈空间。 

# 2026.04.27 12:48 

# 题解注释 迭代法 

class Solution:
    # 获取链表长度
    def getListLength(self, head: Optional[ListNode]) -> int:
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    # 分割链表
    # 如果链表长度 <= size，不做任何操作，返回空节点
    # 如果链表长度 > size，把链表的前 size 个节点分割出来（断开连接），并返回剩余链表的头节点
    def splitList(self, head: Optional[ListNode], size: int) -> Optional[ListNode]:
        # 先找到 next_head 的前一个节点
        cur = head
        for _ in range(size - 1):
            if cur is None:
                break
            cur = cur.next

        # 如果链表长度 <= size
        if cur is None or cur.next is None:
            return None  # 不做任何操作，返回空节点

        next_head = cur.next
        cur.next = None  # 断开 next_head 的前一个节点和 next_head 的连接
        return next_head

    # 21. 合并两个有序链表（双指针）
    # 返回合并后的链表的头节点和尾节点
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 用哨兵节点简化代码逻辑
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1  # 把 list1 加到新链表中
                list1 = list1.next
            else:  # 注：相等的情况加哪个节点都是可以的
                cur.next = list2  # 把 list2 加到新链表中
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2  # 拼接剩余链表
        while cur.next:
            cur = cur.next
        # 循环结束后，cur 是合并后的链表的尾节点
        return dummy.next, cur

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.getListLength(head)  # 获取链表长度
        dummy = ListNode(next=head)  # 用哨兵节点简化代码逻辑
        step = 1  # 步长（参与合并的链表长度）
        while step < length:
            new_list_tail = dummy  # 新链表的末尾
            cur = dummy.next  # 每轮循环的起始节点
            while cur:
                # 从 cur 开始，分割出两段长为 step 的链表，头节点分别为 head1 和 head2
                head1 = cur
                head2 = self.splitList(head1, step)
                cur = self.splitList(head2, step)  # 下一轮循环的起始节点
                # 合并两段长为 step 的链表
                head, tail = self.mergeTwoLists(head1, head2)
                # 合并后的头节点 head，插到 new_list_tail 的后面
                new_list_tail.next = head
                new_list_tail = tail  # tail 现在是新链表的末尾
            step *= 2
        return dummy.next 

# 时间复杂度O(n log n) 
# 空间复杂度O(1) 

# 手敲代码 迭代法 

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getListLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next 
        return length 
    
    def splitList(self, head, size):
        cur = head 
        for _ in range(size - 1):
            if cur is None:
                break
            cur = cur.next 

        if cur is None or cur.next is None: 
            return None 

        next_head = cur.next 
        cur.next = None 
        return next_head 
        
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode() 
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1 
                list1 = list1.next 
            else:
                cur.next = list2 
                list2 = list2.next 
            cur = cur.next 
        cur.next = list1 or list2 
        while cur.next:
            cur = cur.next 
        return dummy.next, cur 

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = self.getListLength(head)
        dummy = ListNode(next = head) 
        step = 1
        while step < length:
            new_list_tail = dummy 
            cur = dummy.next 
            while cur: 
                head1 = cur 
                head2 = self.splitList(head1, step)
                cur = self.splitList(head2, step)
                head, tail = self.mergeTwoLists(head1, head2)
                new_list_tail.next = head 
                new_list_tail = tail 
            step *= 2
        return dummy.next 
    
# 时间复杂度O(n log n) 
# 空间复杂度O(1) 

# 时间复杂度依旧是要一步一步分，分成O(log n)步，每一步要排的和不要排的总数为O(n)，总的时间复杂度为O(n log n)。 
# 因为没用递归只用了迭代，所以不需要额外的栈空间，所以空间复杂度是O(1) 

# 现在迭代法只能看一遍题解看懂，然后跟着敲，自己写的话写不出来。 

# 2026.04.27 17:15 