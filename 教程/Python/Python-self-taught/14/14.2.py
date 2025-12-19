#第一版（不太符合作者要求）

class Square:
    def __init__(self,s):
        self.s=s
    def print_size(self):
        return "{} by {} by {} by {}".format(self.s,self.s,self.s,self.s)
square=Square(3)
print(square.print_size())#调用方法就要在后面带括号，只是调用实例变量就不用在后面带括号。

#第二版（作者的解题思路）

class Square:
    def __init__(self,s):
        self.s=s
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s,self.s,self.s,self.s)
square=Square(100)
print(square)
