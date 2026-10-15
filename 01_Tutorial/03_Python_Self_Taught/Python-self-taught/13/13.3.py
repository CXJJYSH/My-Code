#这一版：我自己写了报错之后找Kimi给我修改了一下，虽然输出没问题但我还是不太满意。

class Rectangle:
    def __init__(self,w,l):
        self.w=w
        self.l=l
        print("Created!")
    def calculate_perimeter(self):
        return (self.w+self.l)*2
class Square:
    def __init__(self,s):
        self.s=s
        print("Created!")
    def calculate_perimeter(self):
        return self.s*4
class Shape:
    def __init__(self):
        print("Created!")
    def what_am_i(self):
        print("I am a shape.")
class Rectangle(Shape):
    pass
class Square(Shape):
    pass
Rectangle=Rectangle()
Square=Square()
Rectangle.what_am_i()
Square.what_am_i()

#作者牛逼的答案方法（最关键的点在于我没有在要继承的类后面用括号标出被继承的类，同时混淆了pass的用法；pass应该在两个类的参数相等或相同的时候用）：

class Rectangle(Shape):
    def __init__(self,w,l):
        self.w=w
        self.l=l
        print("Created!")
    def calculate_perimeter(self):
        return (self.w+self.l)*2
class Square(Shape):
    def __init__(self,s):
        self.s=s
        print("Created!")
    def calculate_perimeter(self):
        return self.s*4
class Shape:
    def what_am_i(self):
        print("I am a shape.")
Rectangle=Rectangle(1,2)
Square=Square(3)
Rectangle.what_am_i()
Square.what_am_i()

#同时shell中只有两个"Created!"是因为我只创建了两个对象，之前每次都会打印"Created!"是因为我每次创建对象的时候都用到了打印"Created!"的魔法方法。
