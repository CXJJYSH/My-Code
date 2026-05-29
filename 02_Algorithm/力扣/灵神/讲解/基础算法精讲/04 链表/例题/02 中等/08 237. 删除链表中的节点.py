# 单向链表的定义。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next 

# 不能访问头节点的情况下如何删除指定节点？
# 因为题目中说了“给定节点的值不应该存在于链表中”，
# 所以灵神的巧妙方法就是将要删除的节点的值修改成该节点下一节点的值，然后使原本要删除的节点指向下下个节点，
# 这样就起到了删除节点的效果，虽然实际上是把下一个节点删除了，但是这种方法很巧妙且很有效，非常优雅。

# 中等
# 2025.11.16 11:55 ~ 12:11 花了十五分钟左右。