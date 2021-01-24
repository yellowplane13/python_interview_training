class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        currPtr = self.head
        if self.head is None:
            self.head = Node(data)
            return
            # create new Node
        new_node = Node(data)
        while currPtr.next:
            currPtr = currPtr.next
        currPtr.next = new_node
    
    def printLL(self):
        currPtr = self.head
        while currPtr:
            print(currPtr.data, '->',end='')
            currPtr = currPtr.next