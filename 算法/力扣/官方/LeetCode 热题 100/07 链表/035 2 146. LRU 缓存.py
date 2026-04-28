from typing import OrderedDict

# 标准库法 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        self.cache.move_to_end(key, last = False)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value 
        self.cache.move_to_end(key, last = False)
        if len(self.cache) > self.capacity:
            self.cache.popitem()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# 说实话没太看懂，感觉这已经不是算法而是正常项目开发中会用到的代码了。 

class Node:
    __slots__ = 'prev', 'next', 'key', 'value'

    def __init__(self, key = 0, value = 0):
        self.key = key 
        self.value = value 

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.dummy = Node()
        self.dummy.prev = self.dummy 
        self.dummy.next = self.dummy 
        self.key_to_node = {}

    def get_node(self, key):
        if key not in self.key_to_node:
            return None 
        node = self.key_to_node[key]
        self.remove(node)
        self.push_front(node)
        return node 

    def get(self, key: int) -> int:
        node = self.get_node(key) 
        return node.value if node else -1 

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.value = value 
            return 
        self.key_to_node[key] = node = Node(key, value) 
        self.push_front(node) 
        if len(self.key_to_node) > self.capacity:
            back_node = self.dummy.prev 
            del self.key_to_node[back_node.key]
            self.remove(back_node)
    
    def remove(self, x: Node):
        x.prev.next = x.next 
        x.next.prev = x.prev 
    
    def push_front(self, x):
        x.prev = self.dummy 
        x.next = self.dummy.next 
        x.prev.next = x 
        x.next.prev = x 


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# 时间复杂度：所有操作均为 O(1)。 
# 空间复杂度：O(min(p,capacity))，其中 p 为 put 的调用次数。刚开始调用put会逐渐占用空间，之后可能会达到题目限制的最大值capacity。 

# 2026.04.28 16:13 