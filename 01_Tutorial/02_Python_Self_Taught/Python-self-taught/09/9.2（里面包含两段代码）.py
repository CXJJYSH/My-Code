#使用文件指针
print("接下来请回答问题并且你的回答会被打印出来。")
with open("9.2.1","w+") as f:
    a=input("你叫什么名字？")
    f.write(a+"\n")
    b=input("你是男是女？")
    f.write(b+"\n")
    c=input("你几岁了？")
    f.write(c+"\n")
    f.seek(0)
    print(f.read())

#不使用文件指针
print("接下来请回答问题并且你的回答会被打印出来。")
with open("9.2.2","w")as f:
    a=input("你叫什么名字？")
    f.write(a)
    b=input("你是男是女？")
    f.write(b)
    c=input("你几岁了？")
    f.write(c)
with open("9.2.2","r")as f:
    print(f.read())

#不加换行符就不会换行打印。
#第一个代码块中的 print(f.read()) 已经打印了文件内容并“包含了换行符”，所以第二个代码块中的“提示信息”会和第一个代码块的输出结果隔一行。
