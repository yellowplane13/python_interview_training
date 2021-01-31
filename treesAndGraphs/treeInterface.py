# Use this to create a tree for your practice
#           4
#         /   \
#       5       6
#      / \     /  \
#     7   8   9   10

# ROOT LEFT RIGHT since its "PRE"order traversal, the root comes "PRE" to left and right

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(10)
root.right.left = Node(9)