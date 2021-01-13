
from typing import List
import numpy
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        c = 0
        for i in range(1,n+1):
            print("i = ", i)
            marr = []
            j = 0
            while j < n-i+1:
                print("j = ", j)
                sarr = []
                sarr.append(nums[j:j+i])
                #print(sarr, "sub array")
                print(f"{numpy.prod(sarr)} is product of {sarr}")
                if numpy.prod(sarr) < k:
                    marr.append(sarr)
                    c += 1
                j += 1
            print(marr)
            print (c)


op = Solution()
op.numSubarrayProductLessThanK([1,1,1], 2)