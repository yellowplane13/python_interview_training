#268 LC 
# bruteforce

# from typing import List
# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         n = len(nums)
#         nums.sort()
#         missing_num = None
#         for i in range(n):
#             if i != nums[i]:
#                 missing_num = i
#         return missing_num

# res = Solution()
# op = res.missingNumber([1,0,3])
# print(op)

# TO DO : USING HASH MAPS
# USING GAUSS THEORM

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        intendedSum = n * (n+1)//2
        currSum = sum(nums)
        missingNum = intendedSum - currSum
        return missingNum
res = Solution()
op = res.missingNumber([9,6,4,2,3,5,7,0,1])
print(op)