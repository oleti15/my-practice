arr = [1,3,4,2]

maxStack = []

result = [-1] * len(arr)
print(result)

for i in range(len(arr)-1 , -1 , -1):

    while len(maxStack) !=0 and maxStack[-1] <= arr[i]:
        maxStack.pop()

    if len(maxStack) == 0:
        result[i] = -1
    else:
        result[i] = maxStack[-1]

    maxStack.append(arr[i])


print(result)
    