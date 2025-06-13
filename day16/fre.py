list = [11,12,23,43,43,7,7,7,90]


max_freq = 0
max_freq_element = 0
freq_map = {
}

for i in range(len(list)):
    if list[i] not in freq_map:
        freq_map[list[i]] = 1
    else:
        freq_map[list[i]] += 1

print(freq_map)

for key in freq_map:
    if freq_map[key] > max_freq:
        max_freq = freq_map[key]
        max_freq_element = key

print(max_freq_element)

