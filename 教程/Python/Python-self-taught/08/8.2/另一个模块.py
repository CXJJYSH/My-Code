#模块调用之后为什么不按预期打印输出的问题在睡觉的时候脑子帮我解决了。
import cubed
while True:
    a=input("Enter a number:")
    if a.isdigit():
        a=float(a)
        cubed.f(a)
    else:
        print("You should enter a number!")
        break
