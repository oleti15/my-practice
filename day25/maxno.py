list = [8,2,30,40,5,6,4]

max = list[0]
for i in range(1, len(list)):
    if max < list[i]:
        max = list[i]

print(max)