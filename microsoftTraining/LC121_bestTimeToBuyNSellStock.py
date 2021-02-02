# What we are actually doing is this: for every element, 
# we are calculating the difference between that element and the minimum of all the values 
# before that element and we are updating the maximum profit 
# if the difference thus found is greater than the current maximum profit.

# Don't look to find the selling and the buying pt
# just calculate the differences between the previous index and current index

from typing import List
import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: 
            return 0
        maxProfit = 0
        minVal = float('inf') # give a big 5 digit value since 0<=prices[i]<=10^4 
        
        for price in prices:
            # if price is greater than the minval
            if price > minVal:
                # add the difference to maxProfit
                # the logic being : you buy when the price is at minVal
                # and sell when the price is greater than the minVal
                if maxProfit < price - minVal: #7 - inf X
                    maxProfit = price - minVal # 
                    
            # if price is less than the mininum
            # make this your new buying point, so price becomes the new minval
            elif price < minVal:
                minVal = price
        return maxProfit
    
    #[7,1,5,3,6,4]
    #maxProfit = 4
    #minVal = 1
    #price = 3
    
    
        
        
                
op = Solution()
print(op.maxProfit([7,1,5,3,6,4]))