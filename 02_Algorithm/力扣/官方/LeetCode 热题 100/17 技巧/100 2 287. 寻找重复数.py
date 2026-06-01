from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break 
        
        head = 0
        while slow != head:
            slow = nums[slow]
            head = nums[head]
        
        return slow 
    
# 代码思路是先创建一快一慢两个指针，然后让它们相遇。 
# 根据环形链表题Ⅱ可以知道 相遇点离入环点 和 0初始点（头节点）离入环点 的距离是一样的。 
# 所以相遇后再创建一个头节点指针，让它和慢指针一步一步同时走，相遇的时候就到入环点了。 
# 路径中只有刚开始创建的等于0的head不表示列表中的数，其它都表示列表中的某个数。 
# 指针移动之后的结果都是数字。 
# 相遇点入环点就是列表中重复的那个数。 
# 最后返回入环点的那个数。 

# 时间复杂度O(n) 
# 空间复杂度O(1) 

# 2026.06.01 19:49 