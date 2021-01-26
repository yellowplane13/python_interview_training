# https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#           5
#         /   \
#       3       7
#      / \     /  \
#     2   4   6    8
# insert(5,5.5)
# insert(4,3)


class Tree:
    def insert(self, root, data):
        if root is None:
            root = Node(data)
            return

        if root.data == data:
            return root

        elif root.data < data:
            if root.right is None:
                root.right = Node(data)
            else:
            # if root.right.data < data:
            #     insert(root.right, data)
            # else:
                self.insert(root.right, data)

        else:
        # if root.data > data:
            if root.left is None:
                root.left = Node(data)
                return
            else:
            # if root.left.data > data:
            #     insert(root.left, data)
            # else:
                self.insert(root.left, data)

    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            print(root.data)
            self.inOrder(root.right)


if __name__ == '__main__':
    tree = Tree()
    root = Node(random.randint(0,100))
    print(root.data,":root's val")
    for i in range(10):
        n = random.randint(0,200)
        print("num getting inserted:",n)
        tree.insert(root,n)
    tree.inOrder(root)


# tree = Node(5)
# insert(tree, 3)
# insert(tree, 4)
# insert(tree, 7)
# insert(tree, 6)
# insert(tree, 8)

# preOrder(tree)