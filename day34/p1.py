import heapq
priorq=[]
while True:
    print("Main menu")
    print("1.Add element")
    print("2.delete front element")
    choice=int(input("enter choice(1\2):"))
    if choice==1:
        name=input("enetr name:")
        priority_order=int(input("Enter priority order:"))
        heapq.heappush(priorq,{'name':name,'priority_order':priority_order})
        print(priorq)
    if choice==2:
        heapq.heappop(priorq)
        print(priorq)