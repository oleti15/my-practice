list=[0,1,3,4]
list1=range(0,len(list))
for i in list1:
    if i not in list:
        print(i)