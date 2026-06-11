"""
实验9-2 折半查找验证
要求：查找表必须是有序的
"""

def binary_search(arr, key):
    """
    折半查找（非递归）
    :param arr: 有序列表（升序）
    :param key: 目标值
    :return: 索引 / -1
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


if __name__ == "__main__":
    data = sorted([45, 23, 78, 12, 56, 89, 34])  # 必须先排序
    target = 56

    print("有序序列:", data)
    pos = binary_search(data, target)

    if pos != -1:
        print(f"元素 {target} 在第 {pos} 位")
    else:
        print(f"元素 {target} 不存在")

# 2026.06.10 10:24 验完了 