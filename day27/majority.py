nums=[2,2,1]
counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1 #use .get increase the num value
    if counts[num] > len(nums) // 2:
        print(num)