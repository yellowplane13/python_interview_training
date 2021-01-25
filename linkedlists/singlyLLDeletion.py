# One thing to remember here is that every Node is an object. 
# That means, if you print currPointer.next, you'll get an object as a result because it holds the next  HeadNode 
#                                                                                                          /\
#                                                                                                         |  |
#                                                                                                      data (nextNode)
#                                                                                                               /\
#                                                                                                             |    |
#                                                                                                          data   nextNode


class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_head(self, data):
        self.head = Node(data, self.head)
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
        else:
            currPointer = self.head
            while currPointer.next:
                currPointer = currPointer.next
            currPointer.next = Node(data,None)
    
    def printLL(self):
        if self.head is None:
            print("Nothing to see here")
        else:
            currPointer = self.head
            while currPointer:
                print(currPointer.data, "-->", end='')
                currPointer = currPointer.next
            print(" None")
    
    def delete(self,data):
        if self.head is None:
            print("Nothing to delete here")
        else:
            # if there is a LL present, set two pointers
            currPointer = self.head
            prevPointer = None
            
            while currPointer.next:
                print("Data at Head:",currPointer.data)
                print("Pointer at Head:",currPointer.next.data)
                if currPointer.data == data:
                    if currPointer.next is None:
                        prevPointer.next = None
                        break
                    else:
                        #if you're deleting the head
                        if currPointer.data == self.head.data:
                            prevPointer = self.head.next
                            self.head = prevPointer
                        else:
                            # if the node being deleted is not at the head
                            prevPointer.next = currPointer.next
                            print("prevPtr: ",prevPointer.data)
                            print("deleting the node: ", currPointer.data)
                prevPointer = currPointer
                currPointer = currPointer.next
            

newLL = LinkedList()
newLL.insert_at_end(3)
newLL.printLL()
newLL.insert_at_end(8)
newLL.printLL()
newLL.insert_head(0)
newLL.printLL()
newLL.insert_at_end(13)
newLL.printLL()
newLL.delete(0)
newLL.printLL()
