# arr=[1,2,3,4,5]
# target=9
# n=len(arr)
# for i in range(0,n):
#     for j in range(i+1,n):
#        if arr[i]+arr[j]==target:
#         print([i,j])
#         break
        

#two pointers
# arr=[1,2,3,4,5]
# n=len(arr)
# target=9
# left=0
# right=n-1
# while left<right:
#     if arr[left]+arr[right]==target:
#         print([left,right])
#     elif arr[left]+arr[right]<target:
#         left+=1
#         break

list=[1,2,3,4,5]
target=9
dict={}
for i in range(len(list)):
    dict(list[i])==i
for i in range(len(list)):
    find=target-list[i]
    if find in dict and dict[find]!=i:
        print([i,dict[find]])
        break