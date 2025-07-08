# def sum(n):
#     if n==0:
#         return 0
#     return n+sum(n-1)
# print(sum(5))


# def fact(n):
#     if n==0 or n==1:
#         return n
#     return n*fact(n-1)
# print(fact(5))

def fib(n):
    if n==1 or n==0:
        return n
    return fib(n-1)+fib(n-2)
print(fib(4))      # tc=>2^n