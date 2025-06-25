# print("*")
# Triangle combinations of triangles 
# n=4
                                    # *
                                    # * *
                                    # * * *
                                    # * * * *
                                    # * * *
                                    # * *
                                    # *
                                    # 
# for i in range(n): 
#     for j in range(i+1):
#         print("*",end=" ") 
#     print()
# for i in range(n,0,-1):
#     for j in range(i-1):
#         print("*", end=" ")
#     print()



                                                            
                                                                                                                                
# n=4                                                         
# for i in range(n+1):                                        
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()


# reverse a triangle:
# 
# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()






#this a square
# for i in range(3):
#     for j in range(3):
#         print("*",end=" ")
#     print()







#This is a pyramid

# n=4
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(2*i-1):
#         print("*",end=" ")
#     print()






# reverse a pyramid
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




# string pyramid
# str="A"
# n=5                     #no.of rows
# for i in range(n):       #outer loop
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     s=(ord(str))
#     for j in range(2*i+1):
#         print(chr(s),end=" ")
#         s+=1
#     print()


   

