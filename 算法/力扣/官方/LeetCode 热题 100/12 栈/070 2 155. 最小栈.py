from cmath import inf

class MinStack:

    def __init__(self):
        self.st = [(0, inf)]
        
    def push(self, val: int) -> None:
        self.st.append((val, min(self.st[-1][1], val)))

    def pop(self) -> None:
        self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][-1]

# 时间复杂度O(1)，所有操作均为O(1)。 
# 空间复杂度O(q)，q为push调用的次数。 

# 2026.05.19 11:24 