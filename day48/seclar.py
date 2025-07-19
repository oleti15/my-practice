#second largest element in a given list
numbers = [10, 20, 4, 45, 99, 99]
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
if len(unique_numbers) >= 2:
    second_max = unique_numbers[1]
    print("Second maximum number is:", second_max)
else:
    print("List doesn't have enough unique elements.")