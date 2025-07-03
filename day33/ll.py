class Node:
    def __init__(self , data = 0 , next = None):
        self.val = data
        self.next = next

def display_linked_list(head):
    result = []
    current = head
    while current != None:
        result.append(str(current.val))
        current = current.next
    print(" => ".join(result))

item1 = Node(3)
item2 = Node(5)
item3 = Node(8) #tail node

item1.next = item2 #head
item2.next = item3


head = item1

#traverse

# current = head
# while current != None:
#     # print(current.val , end="=>")
#     current = current.next

# current = head
# length = 0

# while current != None:
#     length += 1
#     current = current.next

# print(length)


# #insert at the start

# newItem = Node(int(input()) , head) #O(1)
# display_linked_list(newItem)
# head = newItem

# #insert at end

# newItem = Node(int(input()))

# current = head
# while current.next != None:
#     current = current.next

# current.next = newItem

# display_linked_list(head)


#insert at position

data = int(input("Enter the data to insert :"))
position = int(input("Enter the POsition to insert : "))

newNode = Node(data)
prev = None
count = 0
current = head

while current != None:
    count += 1
    if(count == position):    
        prev.next = newNode
        newNode.next = current

    prev = current
    current = current.next

display_linked_list(head)

position = int(input("enter position to del : "))

current = head
prev = None
count = 0
while current != None:
    count += 1
    if position == count:
        prev.next = current.next

    prev = current
    current = current.next

display_linked_list(head)