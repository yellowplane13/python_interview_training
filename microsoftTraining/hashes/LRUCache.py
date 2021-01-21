# 146 leetcode

from collections import deque
class LRUCache:
    def __init__(self, capacity: int):
        self.c = capacity
        #instantiate empty dictionary
        self.dict = {}
        #instantiate empty deque datastructure
        self.deck = deque()
        

    def get(self, key: int) -> int:
        # if key is present, add the key to the beginning of deque
        if key in self.dict:
            self.deck.remove(key)
            self.deck.appendleft(key)
            return (self.dict[key])
        # if key is not in deque, return -1
        else:
            return -1
            
    def put(self, key: int, value: int) -> None:
        # if key is in deque, add it to the beginning of deque
        # and update value
        if key in self.dict:
            self.deck.remove(key)
            self.deck.appendleft(key)
            self.dict[key] = value
        else:
            # first check if the capacity has reached 
            # if it has, remove the least referenced one from the end using pop and update
            # else: 
            # append the deque in the beginning with the key 
            # and update the dictionary with the key, value pair
            if len(self.dict) < self.c:
                self.deck.appendleft(key)
                self.dict[key] = value
            else:
                poppedval = self.deck.pop()
                del self.dict[poppedval]
                self.deck.appendleft(key)
                self.dict[key] = value
        
        


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
param_1 = obj.get(2)
print(param_1)
obj.put(1,1)
obj.put(3,3)
obj.put(2,2)
print (obj.dict)

#operations to test
#["LRUCache","put","put","get","put","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]