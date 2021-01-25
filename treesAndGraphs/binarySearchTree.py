#https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None 

#           5
#         /   \
#       3       7
#      / \     /  \
#     2   4   6    8
# insert(5,5.5)
#insert(4,3)

def insert(root, data):
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
            insert(root.right,data)
    
    else:
        # if root.data > data:
        if root.left is None:
            root.left = Node(data)
            return
        else:
            # if root.left.data > data:
            #     insert(root.left, data)
            # else:
            insert(root.left,data)
    

def preOrder(root):
    if root is not None:
        print(root.data)
        preOrder(root.left)
        preOrder(root.right)

tree = Node(5)
insert(tree,3)
insert(tree,4)
insert(tree,7)
insert(tree,6)
insert(tree,8)

preOrder(tree)























# class BinarySearchTree:
#     # Initialize an empty tree
#     def __init__(self):
#         self.root = None
        
#     # we do the insert recursively
#     # check if self.root exists, if it does, search down tree from there recursively 
#     # using private _insert function to do the recurisive calls
#     def insert(self, data):
#         if self.root is None:
#             self.root = Node(data)
#         else:
#             self._insert(data, self.root)

#     def _insert(self,data,currNode):
#         if data < currNode.data:
#             if currNode.left != None:
#                 self._insert(data,currNode.left)
#             else:
#                 currNode.left = Node(data)
        
#         elif data > currNode.data:
#             if currNode.right != None:
#                 self._insert(data,currNode.right)
#             else:
#                 currNode.right = Node(data)
#         else:
#             print(f"Current data {data} passed already in the tree")

#     def printList(self):
#         if self.root is None:
#             print("the tree is empty")
#         else:
#             ("getting into _print function")
#             #print(self.root.data)
#             self._printList(self.root)
    
#     def _printList(self, currNode):
#         if currNode.left != None:
#             print("the value to be inserted is : ", currNode.left.data)
#             self._printList(currNode.left)
#             print(str(currNode.data))
#             self._printList(currNode.right)
#         #     print(currNode.data)
#         #     self._printList(currNode.left)
#         # elif currNode.right != None:
#         #     print(currNode.data)
#         #     self._printList(currNode.right)

#     def fillTree(self, tree, n = 10, maxInt = 20):
#         from random import randint
#         for _ in range(0,n):
#             currElement = randint(0,maxInt)
#             tree.insert(currElement)
#             print("the element getting iserted into tree", currElement)
#         return tree
    
# tree = BinarySearchTree()
# tree = tree.fillTree(tree)
# tree.printList()
