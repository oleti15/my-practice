list=[2,3,0,4,0,5,6,0,2]
result=[]
for i in range(len(list)):
    if list[i]!=0:
        result.append(list[i])
noofzeros=list.count(0)
for i in range(noofzeros):
    result.append(0)
print(result)



