longest=0
arr=[-1,-1,2,0,4,-1,8]
target=3
sum = 0
prefix_sum = {}
arr = [-10,-1,-1,2,0,4,-1,8]
for x in range(0 , len(arr)):
    sum += arr[x]
    if sum == target:
        longest = x + 1
    else:
        if (sum - target) in prefix_sum:
            longest = max(longest , x - prefix_sum[sum-target])
    if sum not in prefix_sum:
        prefix_sum[sum] = x

print(arr)
print(longest)