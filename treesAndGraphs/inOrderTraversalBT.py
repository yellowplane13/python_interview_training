#LC 94
# HINT : for "IN"order traversal, the root is "IN"-between left and right, so it is:
# LEFT -> ROOT -> RIGHT
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorderTraverse(node):
    if node is not None:
        inorderTraverse(node.left)
        print(node.data)
        inorderTraverse(node.right)


#           4
#         /   \
#       5       6
#      / \     /  \
#     7 None None None

root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)

inorderTraverse(root)
