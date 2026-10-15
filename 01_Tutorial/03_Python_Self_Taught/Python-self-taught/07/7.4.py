while True:
    guess=input("Guess a number(You can also enter 'q' to quit.):")
    list=[]
    for i in range(0,100):
        i=str(i)
        list.append(i)
    if guess in list:
        print("True!")
    elif guess=='q':
        break
    else:
        print("Not found.")
#append方法没有返回值，所以用[列表]=[列表].append([元素])不会产生预期想要产生的新列表。
