



# - Reverse the list
my_list = [1, 2, 3, 4, 5]    ## Method 1: Using slicing
reversed_list = my_list[::-1]
print(reversed_list)  # Output: [5, 4, 3, 2, 1]

my_list.reverse()   ## Method 2: Using reverse() method
print(my_list)  # Output: [5, 4, 3, 2, 1]


for item in reversed(my_list):    ## Method 3: Using reversed() function
    print(item)

# - Find the middle element
# - Detect cycles
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# - Merge sorted lists
# - Sort using merge sort
