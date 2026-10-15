class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        last=len(self.items)-1
        return self.items[last]
    def size(self):
        return len(self.items)

stack=Stack()
for i in range(1,6):
    stack.push(i)
reverse=[]
for i in range(len(stack.items)):
    reverse.append(stack.pop())
print(reverse)
#沃趣！竟然大功告成一遍过！我还以为会有啥意想不到的报错呢。看来还是学到了一点东西的^_^
