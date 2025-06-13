list = [11,12,23,43,43,7,7,7,90]
print(set(list))

max_freq = 0
max_freq_element = 0

#n^2 soln:

for i in range(0, len(list)):
    count = 1
    for j in range(i +1  , len(list)):
        if list[i] == list[j]:
            count += 1
     #  j loop ends over here
    if max_freq < count:
        max_freq = count
        max_freq_element = list[i]

