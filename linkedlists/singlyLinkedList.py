# create nodes
# add nodes 
# remove nodes
# print linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create linked list
class LinkedList: 
    def __init__(self):
        self.head = None #initally ll is empty

    def addNode(self, node):
            if self.head is None:
                self.head = node
                #self.head.next = None
                #print(self.head.data)
            else:
                findLastNode = self.head
                while True:
                    if findLastNode.next is None:
                        break
                    else:
                        findLastNode = findLastNode.next #advance to the next node in the LL
            
                #print(findLastNode.data)
                findLastNode.next = node 

    
    def printList(self):
        currNode = self.head
        while True:

            if currNode is None:
                break
            else:
                print(currNode.data)
                currNode = currNode.next

    def addHeadNode(self, newNode):
        tempNode = self.head
        self.head = newNode
        newNode.next = tempNode
        del tempNode

    def addNodeAt (self, nn, pos):
        c = 0
        currN = self.head
        while True:
            if c == pos:
                break
            else:
                prevN = currN
                currN = currN.next
                c += 1
        
        prevN.next = nn
        nn.next = currN


ll = LinkedList()

node1 = Node("a")
ll.addNode(node1)

node2 = Node("b")
ll.addNode(node2)

node3 = Node("c")
ll.addNode(node3)

node4 = Node("e")
ll.addNode(node4)


# node5 = Node("0")
# ll.addHeadNode(node5)

node6 = Node("d")
ll.addNodeAt(node6, 3)

node7 = Node("ab")
ll.addNodeAt(node7, 1)

ll.printList()