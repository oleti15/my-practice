# string="abc"
# def set(index,subset):
#     if index==len(string):
#         print(''.join(subset))
#         return
#     subset.append(string[index])
#     set(index+1,subset)
#     subset.pop()
#     set(index+1,subset)
# set(0,[])




#combination sum
arr=[1,1,2]
k=2
def set(index,subset,subsum):
    if index==len(arr):
        if subsum==k:
            print(subset)
        return
    subset.append(arr[index])
    set(index+1,subset,subsum+arr[index])
    subset.pop()
    set(index+1,subset,subsum)
set(0,[],0)
 