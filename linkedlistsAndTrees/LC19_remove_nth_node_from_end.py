# LC 19
# https://www.youtube.com/watch?v=tk6fo3Z-qkQ&ab_channel=SuboptimalEngineer
# Definition for singly-linked list.

from LC_linkedList_Interface import Node, LinkedList

class removeNode(LinkedList):

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

    def removeNthFromEnd(self, head: Node, n: int) -> Node:
        # 3 steps to this
        
        # Step 1 : find the number of nodes in the ll
        len = 0
        curr = self.head
        print(self.head)
        while curr:
            curr = curr.next
            len += 1
        # calculate the node that has to be removed frm the beginning
        # (len - n)th node
        k = len - n
        print("val of k", k)
        
        # step 2 : traverse to the kth node
        currPtr = self.head
        prevPtr = None
        
        # step 2 : traverse to the kth node by decrementing k as you go down the list
        while k != 0:
            prevPtr = currPtr
            currPtr = currPtr.next
            k = k-1
            
        # remove the node
        # if prevPtr is still None after traversing, 
        # that means the node to be removed is the 0th one
        if prevPtr == None:
            return currPtr.next
        else:
            prevPtr.next = currPtr.next
            currPtr.next = None
            currPtr = None
            return head
            

ll = removeNode()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.printLL()
ll.removeNthFromEnd(ll,2)
ll.printLL()