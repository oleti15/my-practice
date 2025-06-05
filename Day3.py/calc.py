import baby as f
a=int(input())
while True:
    op=input()
    if op =="=":
        print("calculator result:",a)
    b=int(input())
if op=="+":
   a=f.add(a,b)
elif op=="-":
    a=f.sub(a,b)
elif op=="*":
    a=f.mul(a,b)
elif op=="div":
    a=f.div(a,b)
elif op=="**":
    a=pow(a,b)
elif op=="%":
    a=f.mod(a,b)
print(a)