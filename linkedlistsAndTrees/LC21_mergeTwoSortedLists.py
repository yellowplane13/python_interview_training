# 21 leetcode
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():

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

    def mergeTwoLists(self, l1, l2):
        ans = Node(0)
        currPtr = ans

        while (l1 and l2):
            if l1.data <= l2.data:
                currPtr.next = l1
                l1 = l1.next
            else:
                currPtr.next = l2
                l2 = l2.next
            
            currPtr = currPtr.next

        while l1:
            currPtr.next = l1
            l1 = l1.next
            currPtr = currPtr.next
        while l2:
            currPtr.next = l2
            l2 = l2.next
            currPtr = currPtr.next

        return ans.next
    


list1 = LinkedList()
list1.append(-9)
list1.append(3)
#list1.append(4)
#list1.printLL()
list2 = LinkedList()
list2.append(5)
list2.append(7)
#list2.append(4)
#list2.printLL()
## NOTICE HOW I FEED IT THE SELF.HEAD INSTEAD OF LIST1 ITSELF.
list1.head = list1.mergeTwoLists(list1.head, list2.head)
list1.printLL()
print()