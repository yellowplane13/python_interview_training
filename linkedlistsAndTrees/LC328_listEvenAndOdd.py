from LC_linkedList_Interface import Node, LinkedList


class evenOdd(LinkedList):
    def __init__(self):
        self.head = None

    def oddEvenList(self, ll: Node) -> Node:

        # 1 ---> 2 ---> 3 ---> 4 ---> 5
        # odd    even
        # self.head   even_head

        # 1 ---> 2 ---> 3 ---> 4 ---> 5
        #       even   odd    odd.next
        # self.head

        oddPtr = self.head
        evenPtr = self.head.next
        even_head = evenPtr

        while evenPtr is not None and evenPtr.next is not None:
            oddPtr.next = evenPtr.next
            oddPtr = oddPtr.next
            evenPtr.next = oddPtr.next
            evenPtr = evenPtr.next

        oddPtr.next = even_head
        return ll

list = evenOdd()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
list.append(6)
list.append(7)
list.append(8)
list.oddEvenList(list)

list.printLL()
[1,2,3,4,5,6,7,8]
