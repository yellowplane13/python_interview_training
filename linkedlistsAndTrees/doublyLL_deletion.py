# Resources:
#https://www.youtube.com/watch?v=Am5u1vaT0x0&list=PL5tcWHG-UPH3nDinW5u_oRcNv6hwhY7ET&index=3&ab_channel=LucidProgramming
# The only difference is I used inheritance and took append function from another class : doublyLL_addAfter_addBefore
from doublyLL_addAfter_addBefore import Node

from doublyLL_addAfter_addBefore import DoublyLinkedList

class DeleteDLL(DoublyLinkedList):
    def __init__(self):
        self.head = None
    
    # 4 different cases to take care of
    def deleteNode(self,key):
        currPtr = self.head
        while currPtr:
            # case 1 : Kill the head when there's only head and no other node
            # case 2 : Kill the head when there's another node attached to it
            if currPtr == self.head and currPtr.data == key:
                if self.head.next is None:
                    # killing the data
                    currPtr = None
                    # killing the pointer to the node
                    self.head = None
                    return
                # case 2: there's another node that needs to inherit head
                else:
                    nextPtr = currPtr.next
                    nextPtr.prev = None
                    currPtr.next = None
                    self.head = nextPtr
                    # delete the head node
                    currPtr = None
                    return
            currPtr = currPtr.next
            #case 3: if currPtr.next is not None
            # if the node to be deleted is the last node
            # traverse to the end
            if currPtr.data == key and currPtr.next is None:
                prevPtr = currPtr.prev
                prevPtr.next = None
                currPtr.prev = None
                currPtr = None
                return
            #case 4: if currPtr.next is not None
            # if the node to be deleted is in the middle
            # traverse to the end
            if currPtr.data == key and currPtr.next is not None:
                prevPtr = currPtr.prev
                nextPtr = currPtr.next
                prevPtr.next = nextPtr
                nextPtr.prev = prevPtr
                # delete everything about the currPtr
                currPtr.next = None
                currPtr.prev = None
                currPtr = None
                return

dd = DeleteDLL()
dd.append(1)
dd.prepend(0)
dd.append(2)
dd.append(3)
dd.printLL()
dd.deleteNode(0)
dd.printLL()
dd.deleteNode(2)
dd.printLL()
dd.deleteNode(3)
dd.printLL()
dd.deleteNode(1)
dd.printLL()

# output
#0 <->1 <->2 <->3 <->
#1 <->2 <->3 <->
#1 <->3 <->
#1 <->