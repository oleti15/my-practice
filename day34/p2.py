from collections import deque
queue=deque()

#enqueue
queue.append(5)
print(queue)
queue.append(6)
print(queue)
queue.append(7)
print(queue)

#dequeue
queue.pop()
print(queue)
#peak
print(queue[0])

queue.append(9) # add in rear
queue.popleft() # remove from front
queue.appendleft(7) #add in front
queue.pop()