"""
实验9-1 顺序查找验证
功能：在无序列表中查找指定元素，返回其索引（未找到返回-1）
"""

def sequential_search(arr, key):
    """
    顺序查找算法
    :param arr: 待查找的无序列表
    :param key: 目标值
    :return: 索引 / -1
    """
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == "__main__":
    data = [45, 23, 78, 12, 56, 89, 34]
    target = 56

    print("待查找序列:", data)
    pos = sequential_search(data, target)

    if pos != -1:
        print(f"元素 {target} 在第 {pos} 位")
    else:
        print(f"元素 {target} 不存在")

# 2026.06.10 10:24 验完了 