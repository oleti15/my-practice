num=int(input("enetr a number:"))
sum=0
while num!=0:
    sum+=num%10
    num//=10
if num%sum==0:
    print("Harshad number")
else:
    print("not harshad number")