"""
实验9-3 二叉排序树的建立
功能：插入节点并中序遍历（输出有序序列）
"""


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """插入节点"""
        if not self.root:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left:
                self._insert(node.left, key)
            else:
                node.left = BSTNode(key)
        else:
            if node.right:
                self._insert(node.right, key)
            else:
                node.right = BSTNode(key)

    def inorder(self):
        """中序遍历"""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


if __name__ == "__main__":
    bst = BinarySearchTree()
    data = [45, 23, 78, 12, 56, 89, 34]

    for x in data:
        bst.insert(x)

    print("原始序列:", data)
    print("二叉排序树中序遍历结果:", bst.inorder())

# 2026.06.10 10:24 验完了 