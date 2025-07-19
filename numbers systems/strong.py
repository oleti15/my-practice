import math
num=int(input("Enter a number:"))
sum=0
for i in str(num):
    sum+=math.factorial(int(i))
if sum==num:
    print("strong number")
else:
    print("Not strong number")