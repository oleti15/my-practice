l=[2,3,5,7,9,11,14]
x=int(input("enter a number:"))
for i in range(0,len(l)):
    if x==l[i]:
        print(" number is found")
    else:
        print("number not found")
        break