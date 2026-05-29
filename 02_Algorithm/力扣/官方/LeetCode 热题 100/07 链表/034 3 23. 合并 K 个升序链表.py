# Definition for singly-linked list.

from heapq import heapify, heappop, heappush
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

ListNode.__lt__ = lambda a, b: a.val < b.val 

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        h = [head for head in lists if head]
        heapify(h)
        while h:
            node = heappop(h)
            if node.next:
                heappush(h, node.next)
            cur.next = node 
            cur = cur.next 
        return dummy.next 
    
# 时间复杂度：O(L log m)，其中 m 为 lists 的长度，L 为所有链表的长度之和。每次取出最小元素要O(log m)的时间复杂度，一共操作L个节点次。 
# 空间复杂度：O(m)，堆中至多有 m 个元素。 

# 2026.04.28 15:03 

# 这道题的其它方法之后再去看。
# https://leetcode.cn/problems/merge-k-sorted-lists/description/?envType=study-plan-v2&envId=top-100-liked。 

# 2026.04.28 15:04 