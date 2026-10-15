#第一版：将“半径”这个实例变量放在了方法“area”里，并且没有使用pi函数。

import math

class Circle:
    def __init__(self):
        print("Created!")
    def area(self,r):
        self.radius=r
        return self.radius*self.radius*3.14
Circle=Circle()
print(Circle.area(10))

#第二版：将“半径”这个实例变量放在了魔法方法“__init__”里，并且没有使用pi函数。

import math

class Circle:
    def __init__(self,r):
        self.radius=r
        print("Created!")
    def area(self):
        return self.radius*self.radius*3.14
Circle=Circle(10)
print(Circle.area())

#第三版：将“半径”这个实例变量放在魔法方法“__init__”里，并且使用了pi函数。

import math

class Circle:
    def __init__(self,r):
        self.radius=r
        print("Created!")
    def area(self):
        return self.radius*self.radius*math.pi
Circle=Circle(10)
print(Circle.area())
