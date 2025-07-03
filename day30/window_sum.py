# arr=[2,10,15,0,9,3,1]
# k=4
# maximum=0
# window_sum=0
# n=len(arr)
# for i in range(0,k):
#     window_sum+=arr[i]
#     maximum=window_sum
# for i in range(k,n):
#     window_sum=window_sum+arr[i]-arr[i-k]
#     maximum=max(window_sum,maximum)
# print(maximum)




# j+=1 explore elements
# i+=1 condition fail



arr = [2, 1, 1, 4, 3]
target = 7
n = len(arr)
i = 0
j = 0
min_len = n + 1
window_sum = 0

for j in range(n):
    window_sum += arr[j]
    while window_sum >= target:
        min_len = min(min_len, j - i + 1)
        window_sum -= arr[i]
        i += 1

print(min_len if min_len != n + 1 else 0)
