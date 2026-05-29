from heapq import heappush, heappush_max, heappushpop, heappushpop_max

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            heappush_max(self.left, heappushpop(self.right, num))
        else:
            heappush(self.right, heappushpop_max(self.left, num)) 

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[0]
        return (self.left[0] + self.right[0]) / 2        

# 问了Gemini之后看懂了。 
# https://gemini.google.com/app/35da423d2d71ce57 

# 时间复杂度O(log q)，初始化和findMedian都是O(1)，addNum是O(log q)，q是addNum的调用次数，每次操作堆需要O(log q)的时间。 
# 空间复杂度O(q) 

# 2026.05.21 22:26 