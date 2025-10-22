from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

def dfs(node: Optional[TreeNode], depth: int = 0) -> Optional[TreeNode]:
    indent = "  " * depth
    print(f"{indent}Enter node {node.val if node else None}")

    # 空节点，直接返回 None
    if node is None:
        print(f"{indent}  -> return None")
        return None

    # 递归左右子树
    left = dfs(node.left, depth + 1)
    right = dfs(node.right, depth + 1)

    # 打印本层看到的左右结果
    print(f"{indent}  left={left.val if left else None}, right={right.val if right else None}")

    # 简单示例：总是返回当前节点，你可以改成自己的逻辑
    print(f"{indent}  -> return node {node.val}")
    return node

# 手动构造一棵示例树
#       3
#      / \
#     5   1
#    /   /
#   6   0
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.right.left = TreeNode(0)

    print("=== 开始递归 ===")
    dfs(root)
    print("=== 递归结束 ===")
