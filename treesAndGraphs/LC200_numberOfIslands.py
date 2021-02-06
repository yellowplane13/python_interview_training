# https://www.youtube.com/watch?v=uDB5QXTqMn0&ab_channel=DEEPTITALESRA
from typing import List
class Solution:
    def dfs(self,grid,r,c):
        print(grid[r][c],f"setting grid at {r},{c} to 0")
        grid[r][c] = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for dx,dy in directions:
            x = r+dx
            y = c+dy
            
            if x >= 0 and x<len(grid) and y >= 0 and y < len(grid[0]):
                if grid[x][y] == '1':
                    print("recursive on")
                    self.dfs(grid,x,y)
                    
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                print(grid[r][c],f"grid at {r},{c}")
                if grid[r][c]=='1':
                    print("initial call")
                    self.dfs(grid,r,c)
                    islands += 1
                    print(islands,"islands")
        return islands
        
op = Solution()
print(op.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
print(op.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))