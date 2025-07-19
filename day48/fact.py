num=int(input("Enter a number : "))
fact=1
if num<0:
    print("factorial does not exit nagitive numbers")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range(2,num+1):
        fact=fact*i
    print("The number is factoril",{fact})