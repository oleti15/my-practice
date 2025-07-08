# def Fun(count,end):
#     if count==end:  #base condition
#         return 
#     print(count)   #operation
#     count-=1
#     Fun(count,end)   #recursive fun call
#   Fun(5,0)
def jaya(n):
    if n==0:  #base condition
        return 
    jaya(n-1)  #recursive fun call
    print(n)   #operation
jaya(5)
