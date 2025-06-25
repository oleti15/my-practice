arr=[1,2,3,4,6]
arr1=[5,7,8,9,10]
result=[]
l1=len(arr)
l2=len(arr1)
x=0
y=0
while x<l1 and y<l2:
    if arr[x]<arr1[y]:
        result.append(arr[x])
        x+=1
    else:
        result.append(arr1[y])
        y+=1
while x < l1:
    result.append(arr[x])
    x += 1

while y < l2:
    result.append(arr1[y])
    y += 1

print(result)

    