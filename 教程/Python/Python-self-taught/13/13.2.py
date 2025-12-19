#第一版（自己写的）

class Square:
    def __init__(self,s):
        self.s=s
        print("Created!")
    def change_size(self,n):
        self.n=n
        return self.s+self.n
Square=Square(10)
print(Square.change_size(-3))

#第二版（答案的方法）

class Square:
    def __init__(self,s):
        self.s=s
        print("Created!")
    def change_size(self,n):
        self.s+=n
Square=Square(10)
print(Square.s)
Square.change_size(-3)
print(Square.s)
