from collections import deque
class TreeNode():
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

# #DFS
# def PreOrder(root):
#     if root==None:
#         return 
#     print(root.val,end=" ")
#     PreOrder(root.left)
#     PreOrder(root.right)

# def Inorder(root):
#     if root==None:
#         return
#     Inorder(root.left)#left
#     print(root.val,end=" ")
#     Inorder(root.right)
# def PostOrder(root):
#     if root==None:
#         return
#     PostOrder(root.left)
#     PostOrder(root.right)
#     print(root.val,end=" ")
#BFS
def BFS(root):
    queue=deque([root])
    while queue:
        current=queue.popleft()
        print(current.val,end=" ")
        if current!=None:queue.append(current.left)
        if current!=None:queue.append(queue.right)


def Height(root):
    if root==None:
        return
    left_height=Height(root.left)
    right_height=Height(root.right)
    if left_height-right_height<=1:
        return True
    else:
        return False


root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.right=TreeNode(6)
root.left.left.left=TreeNode(9)
root.left.left.right=TreeNode(10)
root.left.right.right=TreeNode(11)
root.right.right.left=TreeNode(7)
root.right.right.right=TreeNode(8)
# print(root.val)
# print(root.left.val)
# print("\n PRE ORDER")
# PreOrder(root)
# print("\n IN ORDER")
# Inorder(root)
# print("\n POST ORDER")
# PostOrder(root)


print("\n BREADDTH FIRST SEARCH")
BFS(root)
