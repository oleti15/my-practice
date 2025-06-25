arr=[1,2,3,4,6]
arr1=[2,3,4,1,7]
result=[]
l1=len(arr)
l2=len(arr1)
x=0
y=0
while x<l1 and y<l2:
    if arr[x]==arr1[y]:
        result.append(arr[x])
        x+=1
        y+=1
    elif arr[x] < arr1[y]:
            x += 1
    else:
            y += 1
print(result)    