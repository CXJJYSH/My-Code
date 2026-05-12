class Node:
    __slots__ = 'son', 'end'

    def __init__(self):
        self.son = {}
        self.end = False 

class Trie:
    def __init__(self):
        self.root = Node() 

    def insert(self, word: str) -> None:
        cur = self.root 
        for c in word:
            if c not in cur.son:
                cur.son[c] = Node() 
            cur = cur.son[c]
        cur.end = True 

    def find(self, word):
        cur = self.root 
        for c in word:
            if c not in cur.son:
                return 0 
            cur = cur.son[c]
        return 2 if cur.end else 1

    def search(self, word: str) -> bool:
        return self.find(word) == 2

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) != 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# 时间复杂度O(n)，时间复杂度：初始化为 O(1)，insert 为 O(n∣Σ∣)，其余为 O(n)，其中 n 是 word 的长度，∣Σ∣=26 是字符集合的大小。注意创建一个节点需要 O(∣Σ∣) 的时间（如果用的是数组）。 
# 空间复杂度O(qn∣Σ∣)，q 是 insert 的调用次数。 

# 2026.05.12 11:55 

# 问了Gemini前缀树是什么及它的运行逻辑后再去看一遍就差不多看懂了。 

# 实际上是二十六叉树，从root开始展开二十六个分支，每个分支继续展开二十六个分支， 
# 查找的时候就是每一层找一个对应的字母，之前没创建代表该字母的节点就创建一下，找到了就继续往下找， 
# 完全找到了就把end设为True表示完全匹配，只找到了部分前缀就把end设为False表示只有前缀匹配， 
# find函数不同的返回值可以用来给search和startsWith函数使用。 

# 2026.05.12 12:07 