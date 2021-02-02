
"""
https://www.youtube.com/watch?v=L2wOEvjCjwA&ab_channel=MagedHelmy
algorithm
step1: add a clone node inbetween each node
currPtr = head
    while head is not None:
        cloneNode = Node(currPtr.val,currPtr.next,currPtr.random)
        tmp = currPtr.next
        currPtr.next = cloneNode
        cloneNode.next = tmp
        
        currPtr.next = cloneNode.next
step2: set random pointers to each of the cloned nodes
while currPtr:
    if currPtr.random: 
        currPtr.next.random = currPtr.random.next
    currPtr.next = currPtr.next.next
    
step3: separate the cloned nodes from the original
create a dummy node
dummy = Node(0)
prev = dummy
currPtr = head
while currPtr:
    prev.next = currPtr.next
    currPtr.next = currPtr.next.next
    currPtr =  currPtr.next
    prevPtr = prevPtr.next

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # step1:
        currPtr = head
        
        while currPtr:
            # create a clone node of currPtr
            cloneNode = Node(currPtr.val, currPtr.next,currPtr.random)
            tmp = currPtr.next
            currPtr.next = cloneNode
            cloneNode.next = tmp
            # increment the currPtr
            currPtr = tmp
        
        # reset currPtr to head
        currPtr = head
        
        #Step 2: assign random pointers correctly to the cloned nodes
        while currPtr:
            if currPtr.random:
                currPtr.next.random = currPtr.random.next
            currPtr = currPtr.next.next
            
        # reset currPtr to head
        currPtr = head
        #step3: separate the nodes
        dummyNode = Node(0)
        prevPtr = dummyNode
        
        while currPtr:
            prevPtr.next = currPtr.next
            currPtr.next = currPtr.next.next
            #increment the currPtr and the prevPtr
            currPtr = currPtr.next
            prevPtr = prevPtr.next
            
        return dummyNode.next
        
        
        