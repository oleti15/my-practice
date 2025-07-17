num = int(input("Enter a number: "))
original = num
visited = set()
while num != 1 and num not in visited:
    visited.add(num)
    sum_of_squares = 0
    while num > 0:
        digit = num % 10
        sum_of_squares += digit ** 2
        num //= 10
    num = sum_of_squares
if num == 1:
    print(f"{original} is a happy number")
else:
    print(f"{original} is not a happy number")
