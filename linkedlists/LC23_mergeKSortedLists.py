# LC #23
# 
# https://www.youtube.com/watch?v=STswQAHV0OE&ab_channel=TimothyHChang - really simple brute force method
# Have a separate fucntion for merging 2 lists. 
# Have an output list that stores the final list
# Merge this output list with each list in a for loop


##################################################
# TODO
# DEBUG WHY THIS DOESN'T WORK
# PS: IT WORKS ON LEETCODE
##################################################
from LC_linkedList_Interface import Node, LinkedList
from typing import List

class mergedKLists(LinkedList):

    def mergeKLists(self, lists):
        # cover the two corner cases
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        # Here, merge each "list" in the array "lists" with the output list oplist. 
        opList = lists[0]
        for i in range(1,len(lists)):
            opList = self.merge2lists(opList, lists[i])
        return opList

    def merge2lists(self, l1, l2):
        headNode = Node(0)
        currPtr = headNode
        while l1 and l2:
            if l1.data <= l2.data:
                currPtr.next = l1
                l1 = l1.next
                currPtr = currPtr.next
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
        return headNode.next
    

list1 = mergedKLists()
list1.append(1)
list1.append(4)
list1.append(5)
list1.printLL()
list2 = mergedKLists()
print()
list2.append(1)
list2.append(3)
list2.append(4)
list2.printLL()
list3 = mergedKLists()
print()
list3.append(2)
list3.append(6)
list3.printLL()
print()

#list2.append(4)
#list2.printLL()
lists = [list1,list2,list3]
print()
op = list1.mergeKLists(lists)

op.printLL()
