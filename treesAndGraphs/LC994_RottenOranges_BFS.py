##############
# Not Complete
##############
'''
variables initialized
----------------------
rowLen
colLen
freshOrangesCount
rottenQueue
level --> which is the output

step1:
-----
loop over the grid, and add rotten oranges to the rottenQueue
add fresh oranges to freshOrangesCount

step2: process the rotten oranges queue
-----
2.a - while the queue is not empty and the fresh oranges > 0
        - increment level / level++
    - calculate the adjecent oranges to the rotten one
    - reduce the fresh orange count 
    - add the newly rotten oranges to the queue
'''
from typing import List
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rowLen = len(grid)
        colLen = len(grid[0])
        level = 0
        rottenQueue = deque()
        freshOrangeCount = 0
        
        #step1:
        for i in range(rowLen):
            for j in range(colLen):
                if grid[i][j] == 2:
                    rottenQueue.append((i,j))
                if grid[i][j] == 1:
                    freshOrangeCount+=1
        #step2:
        while rottenQueue and freshOrangeCount > 0:
            level+=1
            # calc distances of the adjecent cells
            for _ in range(len(rottenQueue)):
                x, y = rottenQueue.popleft()
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    xx = x+dx
                    yy = y+dy
                    print(xx,yy)
                    if xx < 0 or xx >= colLen or yy >= rowLen or yy < 0:
                        continue
                    if grid[xx][yy] == 2 or grid[xx][yy] == 0:
                        continue
                    if grid[xx][yy] == 1:
                        grid[xx][yy] = 2
                        freshOrangeCount-=1
                        rottenQueue.append((xx,yy))
        print(freshOrangeCount)
        #print(rottenQueue)
        print(grid)
        if freshOrangeCount == 0:
            return level
        else:
            return -1
                        
                    
                    