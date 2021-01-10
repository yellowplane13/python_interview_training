# leetcode #283 easy
# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         c = 0
#         for num in nums:
#             if (num != 0):
#                 c += 1
#             else:
#                 nums.remove(num)
#                 nums.append(0)
#         print(nums)



from typing import List
 
class solutions:
    def MoveZeros(self, nums: List[int]):
        j = 0
        for num in nums:
            if (num != 0):
                nums[j] = num
                j += 1
 
        for x in range(j, len(nums)):
            nums[x]= 0
        print(nums)
 
S= solutions()
S.MoveZeros([0,1,12,7,0,21,0,0,4])