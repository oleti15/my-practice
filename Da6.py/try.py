#try:
 #   n=int(input("enter a number:"))
  #  print(f"the number is {n}")
#except exception as error:
 #   print(f"the exception as {error}")
#else:
 #   print("no error occured")
#finally:
 #   print("ok bye program end!")

try:
    n1=int(input())
    n2=input()
    num=n1/n2
    print("num:",num)
except exception as error:
    print(f"Error is {error}")
finally:
    print("program is end")
    
