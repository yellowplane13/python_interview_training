# Resources
# https://www.youtube.com/watch?v=SQHvcLvqq_Q&list=PL5tcWHG-UPH3nDinW5u_oRcNv6hwhY7ET&index=4&ab_channel=LucidProgramming
from doublyLL_deletion import DeleteDLL

from doublyLL_deletion import Node


class ReverseLL(DeleteDLL):
    def __init__(self):
        self.head = None

    def reverse(self):
        currPtr = self.head
        while currPtr:
            tmp = currPtr.prev
            currPtr.prev = currPtr.next
            currPtr.next = tmp
            currPtr = currPtr.prev
        if tmp:
            self.head = tmp.prev
        return


r = ReverseLL()
r.append("B")
r.append("h")
r.append("a")
r.append("r")
r.append("a")
r.append("t")
r.printLL()
r.reverse()
r.printLL()
