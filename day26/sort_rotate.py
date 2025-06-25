lst = [1, 2, 3, 5, 0]
n = len(lst)
k = 0

for i in range(n - 1):
    if lst[i] > lst[i + 1]:
        k = i

arr = [0] * n
for i in range(n):
    arr[(i + (n - k)) % n] = lst[i]

print(arr)


for i in range(0,n-1):
    if lst[i]<lst[i + 1]:
        print("True")
        break
    else:
        print("False")