import heapq
priorq=[]


#enqueue in PQ
heapq.heappush(priorq , 5)  #add to PQ
print(priorq)
heapq.heappush(priorq , 1)
print(priorq)
heapq.heappush(priorq , 2)
print(priorq)
heapq.heappush(priorq , 3)
print(priorq)
heapq.heappush(priorq , 0)
print(priorq)

#dqueue operation
heapq.heappop(priorq)
print(priorq)

while priorq:
    print(heapq.heappop(priorq))

# print("front element : ",priorQ[0]) #peek function

