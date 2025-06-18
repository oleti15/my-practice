list=input().split(",")
print(list)


keyword=input()
# list1=list[1:len(keyword)]
# print(list1)


filterd_List=[]
for x in list:
    if keyword in x:
        filterd_List.append(x)
print(filterd_List)       
