
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        maxFromLeft = []
        maxFromRight = [0] * size
        
        maxVL = float('-inf')
        maxVR = float('-inf')
        
        amtOfWater = 0
        minVal = float('inf')
        diff = 0
        print([i for i in range(size)])
       
        print(height)
        # step1: calculate max array of heights from left
        for h in height:
            maxVL = max(maxVL, h)
            maxFromLeft.append(maxVL)
        
        print(maxFromLeft)
        
        # step2: populate the array with max values from right
        for i in range(size-1,-1,-1):
            maxVR = max(maxVR,height[i])
            maxFromRight[i] = maxVR
            
        print(maxFromRight)
        
        #step3: find min values at each index of maxfromright and maxfromleft arrays
        # find the difference between minvalue from prev step to the height array
        # add the difference to the count var
        
        for i in range(size-1):
            minVal = min(maxFromLeft[i],maxFromRight[i])
            diff = minVal - height[i]
            print(diff,f":diff at {i}")
            #print(height[i],f"height at {i}")
            # case 1:
            if diff > 0:
                amtOfWater += diff
                print(amtOfWater,f":amtOfWater at {i}")
        print(amtOfWater,":final")


rainWater = Solution()
rainWater.trap([0,1,0,2,1,0,1,3,2,1,2,1])
                
                
            