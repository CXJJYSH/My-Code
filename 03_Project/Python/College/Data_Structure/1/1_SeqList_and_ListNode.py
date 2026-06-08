# 2026.06.08 11:22 
# ===================== 顺序表 =====================
class SeqList:
    def __init__(self, maxsize=100):
        self.data = [None] * maxsize
        self.length = 0
        self.maxsize = maxsize

    def clear(self):
        self.length = 0

    def length(self):
        return self.length

    def get(self, i):
        if 0 <= i < self.length:
            return self.data[i]
        return None

    def locate(self, x):
        for i in range(self.length):
            if self.data[i] == x:
                return i
        return -1

    def insert(self, i, x):
        if self.length >= self.maxsize or i < 0 or i > self.length:
            return False
        for j in range(self.length, i, -1):
            self.data[j] = self.data[j - 1]
        self.data[i] = x
        self.length += 1
        return True

    def delete(self, i):
        if i < 0 or i >= self.length:
            return False
        for j in range(i, self.length - 1):
            self.data[j] = self.data[j + 1]
        self.length -= 1
        return True

    def display(self):
        print("顺序表：", end="")
        for i in range(self.length):
            print(self.data[i], end=" ")
        print()


# ===================== 单链表 =====================
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None
        self.length = 0

    def clear(self):
        self.head = None
        self.length = 0

    def get_length(self):
        return self.length

    def get(self, i):
        p = self.head
        while p and i > 0:
            p = p.next
            i -= 1
        return p.data if p else None

    def locate(self, x):
        p, index = self.head, 0
        while p:
            if p.data == x:
                return index
            p = p.next
            index += 1
        return -1

    def insert(self, i, x):
        node = Node(x)
        if i == 0:
            node.next = self.head
            self.head = node
        else:
            p = self.head
            for _ in range(i - 1):
                if not p:
                    return False
                p = p.next
            node.next = p.next
            p.next = node
        self.length += 1
        return True

    def delete(self, i):
        if i == 0 and self.head:
            self.head = self.head.next
            self.length -= 1
            return True
        p = self.head
        for _ in range(i - 1):
            if not p:
                return False
            p = p.next
        if p and p.next:
            p.next = p.next.next
            self.length -= 1
            return True
        return False

    def create_tail(self, values):
        tail = None
        for v in values:
            node = Node(v)
            if not self.head:
                self.head = node
            else:
                tail.next = node
            tail = node
            self.length += 1

    def display(self):
        print("单链表：", end="")
        p = self.head
        while p:
            print(p.data, end=" -> ")
            p = p.next
        print("None")


# ===================== 主程序 =====================
if __name__ == "__main__":
    seq = SeqList()
    seq.insert(0, 10)
    seq.insert(1, 20)
    seq.insert(2, 30)
    seq.display()

    print(seq.length)
    
    print(seq.locate(10))
    seq.delete(0)
    seq.display()
    
    seq.clear()
    seq.display()

    print('顺序表结束')
    print('\n')


    link = LinkList()
    link.create_tail([10, 20, 30])
    link.display()

    print(link.get_length())
    print(link.get(0))

    print(link.locate(20))

    link.insert(3, 40)
    link.display()

    link.delete(2)
    link.display()

    link.clear()
    link.display()

    print('单链表结束')