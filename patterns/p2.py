
# this is a diamond pattern
# n=4
# for i in range(n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print()
# for i in range(n,0,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print()

# number pyramid
# n=4
# for i in range(n+1):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()



#floyd's pyramid
# n=5
# num=1
# for i in range(n+1):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1
#     print()



# rightangle triangle
# n=5
# for i in range(n): 
#     for j in range(i+1):
#         print("*",end=" ") 
#     print()
# for i in range(n,0,-1):
#     for j in range(i-1):
#         print("*", end=" ")
#     print()



#hollow pyramid
# n=6
# for i in range(n+1):
#     for j in range(n-i):
#         print("",end=" ")
#     for j in range(2*i-1):
#         if j == 0 or j == 2 * i - 2 or i == n:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()


#butterfly 
# n=5
# for i in range(n+1):
#     for j in range(i):
#         print("*",end="")
#     for j in range(2*(i-1)):
#         print("",end="")
#     for j in range(i):
#         print(" ",end=" ")
#     print()
# for j in range(i):
#     print("*",end="")
#     for j in range(2*(i-1)):
#         print("",end="")
#     for j in range(i):
#         print(" ",end=" ")
#     print()
