import time
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    # inserting at head means to attach the node to self.head which is what we're doing down below
    def insert_head(self,data):
        self.head = Node(data,self.head)


    def printLl(self):
        if self.head is None:
            print("Empty list")
            return
        currPointer = self.head
        while currPointer:
            print(currPointer.data, '-->', end='')
            currPointer = currPointer.next
        print()


    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data,None)
        else:
            currPointer = self.head
            while currPointer.next:
                currPointer = currPointer.next
            currPointer.next = Node(data, None)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_head(10)
    ll.insert_at_end(20)

    ll.insert_at_end(30)
    ll.printLl()
    ll.insert_head(0)
    ll.printLl()