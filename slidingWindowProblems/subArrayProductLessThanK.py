# ####################
# ##1/13/2021 NOT COMPLETE ####
# It has gone into an infinite loop
# Second solution borrowed from : https://www.geeksforgeeks.org/number-subarrays-product-less-k/
# ####################


# from typing import List
# import numpy
# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         c = 0
#         for i in range(1,n+1):
#             print("i = ", i)
#             marr = []
#             j = 0
#             while j < n-i+1:
#                 print("j = ", j)
#                 sarr = []
#                 sarr.append(nums[j:j+i])
#                 #print(sarr, "sub array")
#                 print(f"{numpy.prod(sarr)} is product of {sarr}")
#                 if numpy.prod(sarr) < k:
#                     marr.append(sarr)
#                     c += 1
#                 j += 1
#             print(marr)
#             print (c)


# op = Solution()
# op.numSubarrayProductLessThanK([1,1,1], 2)



#TRIAL 2
from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        p = 1
        b = 0
        e = 0
        c = 0
        while e < len(nums):
            print("nums[e]",nums[e])
            p *= nums[e]
            print(f"product at {e} is {p}")
            if p < k:
                c+=1
                e+=1
            if p > k:
                p = p//nums[e]
                b+=1
            print("counter:",c)
            print("beg index is:", b)
            print("end index is : ",e)
            #e+=1
        return c

op = Solution()
sol = op.numSubarrayProductLessThanK([1,2,3,4], 16)
print(sol)
