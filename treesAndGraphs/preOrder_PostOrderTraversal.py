#           4
#         /   \
#       5       6
#      / \     /  \
#     7   8   9   10

# ROOT LEFT RIGHT since its "PRE"order traversal, the root comes "PRE" to left and right
from treeInterface import Node

def preOrder(node):
    if (node is not None):
        print(node.data, "->" , end='')
        preOrder(node.left)
        preOrder(node.right)

def postOrder(node):
    if node is not None:
        postOrder(node.left)
        postOrder(node.right)
        print(node.data,"->" , end='')


root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(10)
root.right.left = Node(9)

preOrder(root)
print()
postOrder(root)
print()
#4 ->5 ->7 ->8 ->6 ->9 ->10
