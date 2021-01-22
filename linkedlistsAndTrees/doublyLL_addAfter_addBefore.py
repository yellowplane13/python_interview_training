#Resources:
#https://www.youtube.com/watch?v=dPGBKZBYy0w&list=PL5tcWHG-UPH3nDinW5u_oRcNv6hwhY7ET&index=2&ab_channel=LucidProgramming

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        # if ll is empty
        if self.head is None:
            self.head = Node(data)
            self.head.next = None
        else:
            #traverse to the end of the list
            currPtr = self.head
            while currPtr.next:
                currPtr = currPtr.next
            # create new node
            newNode = Node(data)
            currPtr.next = newNode
            newNode.prev = currPtr
            newNode.next = None
    
    def prepend(self, data):
        # if ll is empty
        if self.head is None:
            self.head = Node(data)
        else:
            currPtr = self.head
            #create new node
            newNode = Node(data)
            newNode.next = currPtr
            newNode.prev = None
            self.head = newNode

    def printLL(self):
        if self.head is None:
            print("nothing to print here")
        else:
            currPtr = self.head
            while currPtr:
                print(currPtr.data, "<->", end="")
                currPtr = currPtr.next
            print()

    def addAfterNode(self,key,data):
        # steps
        # traverse to the node that you want to add after
        # store the details of the curr node, the next node as well as new node
        
        # create new node
        newNode = Node(data)
        #traverse to the node where you want to append the newNode
        if self.head is None:
            self.head = newNode
        else:
            currPtr = self.head
            while currPtr.next:
                currPtr = currPtr.next
                if currPtr.data == key:
                    #store the value of pushedNode
                    pushedNode = currPtr.next

                    #start the transfer of pointers
                    currPtr.next = newNode
                    newNode.prev = currPtr
                    newNode.next = pushedNode
                    pushedNode.prev = newNode
                    print("succeeded squishing process on the right of key")
                    return
        return

    def AddBeforeNode(self,key,data):
        #traverse to the node where you want to append the newNode
        if self.head is None:
            self.head = Node(data)
        # if you have to add the newnode before the head node
        elif self.head.next is None:
            newNode = Node(data)
            newNode.next = self.head
            self.head.prev = newNode
            newNode.prev = None
            self.head = newNode
        else:
            currPtr = self.head
            while currPtr.next:
                currPtr = currPtr.next
                if currPtr.data == key:
                    newNode = Node(data)
                    prevNode = currPtr.prev
                    prevNode.next = newNode
                    newNode.prev = prevNode
                    newNode.next = currPtr
                    currPtr.prev = newNode
                    print("squishing succeeded on the left of key")
                    return
        return


newLL = DoublyLinkedList()
newLL.prepend(0)
newLL.printLL()
newLL.AddBeforeNode(0,-1)
newLL.append(1)
newLL.printLL()
newLL.append(2)
newLL.printLL()
newLL.prepend(-1)
newLL.printLL()
newLL.append(4)
newLL.printLL()
newLL.AddBeforeNode(4,3.5)
newLL.printLL()
newLL.addAfterNode(2,3)
newLL.printLL()

# 0 <->
# -1 <->0 <->1 <->
# -1 <->0 <->1 <->2 <->
# -1 <->-1 <->0 <->1 <->2 <->
# -1 <->-1 <->0 <->1 <->2 <->4 <->
# squishing succeeded on the left of key
# -1 <->-1 <->0 <->1 <->2 <->3.5 <->4 <->
# succeeded squishing process on the right of key
# -1 <->-1 <->0 <->1 <->2 <->3 <->3.5 <->4 <->

