def armstrong(n):
    sum_of_cube=sum(int(digit)**3 for digit in str(n))
    return n==sum_of_cube
n=int(input("Enter a 3-digit number: "))
if armstrong(n):
    print(f"{n} is an Armstrong number")
else:
    print(f"{n}is not an Armstrong number")