# arr=[9,4,2,10,7,8,8,1,9]
# n=len(arr)
# result=1
# max_len=1
# current_len=1
# for i in range(1,n):
#     if arr[i]>arr[i-1]:
#         max_len=current_len+1
#         current_len=1
#     elif arr[i]<arr[i-1]:
#         current_len=max_len+1
#         max_len=1
#     else:
#         max_len-current_len=1
#     result=max(max_len,current_len)
# print(result)

def maxTrublent(arr):
    n = len(arr)
    if n < 2:
        print(n)
    max_len = 1
    curr_len = 1

    for i in range(1, n):
        if i == 1 or (arr[i - 2] < arr[i - 1] > arr[i]) or (arr[i - 2] > arr[i - 1] < arr[i]):
            curr_len += 1
        else:
            curr_len = 2 if arr[i] != arr[i - 1] else 1
        max_len = max(max_len, curr_len)

    print(max_len)

arr=[9,4,2,10,7,8,8,1,9]
print(maxTrublent(arr))