# https://www.youtube.com/watch?v=jKGkphPsnSI&ab_channel=CoreySchafer
# About why to use two stacks to implement this 
# https://stackoverflow.com/questions/2050120/why-use-two-stacks-to-make-a-queue/2050402#2050402

# Peek and push were the hard ones. Revise those
#
# When there's only one thread doing the read/write operation to the stack, there will always be one stack empty. 
# However, in a multi-thread application, if we have only one queue, for thread-safety, either read or write will lock the whole queue. 
# In the two stack implementation, as long as the second stack is not empty, push operation will not lock the stack for pop.
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        
        """
        self.stack1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.stack2 is not None:
            for _ in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())
                print(self.stack2)
            return self.stack2.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack1:
            return self.stack1[0]
        elif self.stack2:
            return self.stack2[-1]
    
    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Input :
#["MyQueue","push","push","peek","pop","empty"]
#[[],        [1],    [2],   [],  [],     []]
# Output
# [null,null,null,1,1,false]

#Input:
#["MyQueue","push","push","peek","pop","empty"]
#[[],[1],[2],[],[],[]]
#
#Expected:
#[null,null,null,1,1,false]

# Input 
# ["MyQueue","push","push","pop","peek"]
# [[],[1],[2],[],[]]
# Output
# [null,null,null,1,2]

# Input
# ["MyQueue","push","push","push","push","pop","push","pop","pop","pop","pop"]
# [[],[1],[2],[3],[4],[],[5],[],[],[],[]]
# Expected:
# [null,null,null,null,null,1,null,2,3,4,5]

# Input
# ["MyQueue","empty"]
# [[],[]]
# Expected:
# [null,true]