# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head 
        fast = head 
        while fast and fast.next: # 检查fast和fast下一指针就好了。 
            slow = slow.next 
            fast = fast.next.next 
            if fast is slow: # 这里 if slow is fast 也行，if fast is slow 更符合算法含义。 
                return True 
        return False 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.04.21 20:41 