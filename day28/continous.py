
nums=[23,2,6,4,7]
n = len(nums)
k=6

for i in range(n):
    total = nums[i]
    for j in range(i + 1, n):
        total += nums[j]
        if k == 0:
            if total == 0:
                print(True) 
        elif total % k == 0:
            print(True)
print(False)

