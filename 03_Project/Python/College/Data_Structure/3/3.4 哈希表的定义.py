"""
实验9-4 哈希表的建立
采用：除留余数法 + 链地址法处理冲突
"""


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        """哈希函数"""
        return key % self.size

    def insert(self, key):
        """插入元素"""
        index = self.hash_func(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def search(self, key):
        """查找元素"""
        index = self.hash_func(key)
        return key in self.table[index]

    def display(self):
        """打印哈希表"""
        for i, bucket in enumerate(self.table):
            print(f"桶 {i}: {bucket}")


if __name__ == "__main__":
    ht = HashTable()
    data = [23, 43, 12, 54, 65, 32, 78]

    for x in data:
        ht.insert(x)

    print("哈希表结构:")
    ht.display()

    target = 54
    print(f"\n查找 {target}:", "存在" if ht.search(target) else "不存在")

# 2026.06.10 10:24 验完了 