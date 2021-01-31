from treeInterface import Node
root = Node(4)
root.left = Node(5)
root.right = Node(6)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(10)
root.right.left = Node(9)

def traverseLeafNodes(root):
    pass
