#第一版：我的低级思路（首先我应该要明确是编写一个“函数”！）

def compare(a,b):
    if a is b:
        print("True")
    else:
        print("False")
compare(1,2)
compare("a","b")
compare("a","a")

#第二版：作者的高级解决方案


def compare(a,b):
    return a is b
print(compare(1,2))
print(compare("a","b"))
print(compare("a","a"))
