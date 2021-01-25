# Resources:
#https://www.youtube.com/watch?v=8kptHdreaTA&list=PL5tcWHG-UPH3nDinW5u_oRcNv6hwhY7ET&index=1&ab_channel=LucidProgramming
class Node():
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.prev = None
        self.next = None
    
    def append(self,data):
        # 4 possible places to insert
        # insert at the end ~ insert by value
        
        #insert at beginning
        if self.head is None:
            self.head = Node(data)
            self.head.prev = None
        else:
            # insert at the end

            #create the new node
            newNode = Node(data)
            currPtr = self.head
            while currPtr.next:
                currPtr = currPtr.next
            newNode.prev = currPtr
            currPtr.next = newNode
            newNode.next = None
    
    def prepend(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            #create the new node
            newNode = Node(data)
            newNode.next = self.head
            self.head.prev = newNode
            newNode.prev = None
            self.head = newNode
        
    def printLL(self):
        if self.head is None:
            print("nothing to print")
        else:
            currPtr = self.head
            while currPtr:
                print(currPtr.data, "<->", end="")
                currPtr = currPtr.next
            print('none')
    

ll = DoublyLinkedList()
ll.append('z')
ll.printLL()
ll.prepend('b')
ll.printLL()
ll.prepend('c')
ll.printLL()
ll.append('d')
ll.printLL()
ll.append('e')
ll.printLL()
