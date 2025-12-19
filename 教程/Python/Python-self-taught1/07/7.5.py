list1=[8,19,148,4]
list2=[9,1,33,83]
list3=[]
for i in list1:
    for j in list2:
        list3.append(i*j)
print(list3)
#append方法没有返回值，所以用[列表]=[列表].append([元素])不会产生预期想要产生的新列表。
