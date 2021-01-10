class Solution:
    # store complements in dict
    def twoSum(self, t, nums):
        compMap ={}
        for i in range(len(nums)):
            comp = t - nums[i]
            if nums[i] in compMap:
                return [compMap[nums[i]], i]
            else:
                compMap[comp] = i
        return

op = Solution()
print(op.twoSum(9,[2,11,7,15]))
