####################
## NOT COMPLETE ####
####################

class Node:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None 

class BinarySearchTree:
    # Initialize an empty tree
    def __init__(self):
        self.root = None
        
    # we do the insert recursively
    # check if self.root exists, if it does, search down tree from there recursively 
    # using private _insert function to do the recurisive calls
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self,data,currNode):
        if data < currNode.data:
            if currNode.leftChild != None:
                self._insert(data,currNode.leftChild)
            else:
                currNode.leftChild = Node(data)
        
        elif data > currNode.data:
            if currNode.rightChild != None:
                self._insert(data,currNode.rightChild)
            else:
                currNode.rightChild = Node(data)
        else:
            print(f"Current data {data} passed already in the tree")

    def printList(self):
        if self.root is None:
            print("the tree is empty")
        else:
            ("getting into _print function")
            #print(self.root.data)
            self._printList(self.root)
    
    def _printList(self, currNode):
        if currNode.leftChild != None:
            print("the value to be inserted is : ", currNode.leftChild.data)
            self._printList(currNode.leftChild)
            print(str(currNode.data))
            self._printList(currNode.rightChild)
        #     print(currNode.data)
        #     self._printList(currNode.leftChild)
        # elif currNode.rightChild != None:
        #     print(currNode.data)
        #     self._printList(currNode.rightChild)

    def fillTree(self, tree, n = 10, maxInt = 20):
        from random import randint
        for _ in range(0,n):
            currElement = randint(0,maxInt)
            tree.insert(currElement)
            print("the element getting iserted into tree", currElement)
        return tree
    
tree = BinarySearchTree()
tree = tree.fillTree(tree)
tree.printList()
