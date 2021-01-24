# https://leetcode.com/problems/subsets-ii/discuss/30166/Simple-python-solution-without-extra-space.
def subsetsWithDup(nums):
    output = [[]]
    last = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            last = [n + [nums[i]] for n in last]
        else:
            last = [n + [nums[i]] for n in output]
        print("last", last)
        output += last
        print(output)
    return output

print(subsetsWithDup([4,4,4,1,4]))
print()
print(subsetsWithDup([1,2,2]))