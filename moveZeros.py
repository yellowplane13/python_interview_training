# leetcode #283 easy
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        for num in nums:
            if (num != 0):
                c += 1
            else:
                nums.remove(num)
                nums.append(0)
        print(nums)