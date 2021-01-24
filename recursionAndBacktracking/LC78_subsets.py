def subsets(nums):
    op = [[]]
    for num in nums:
        op += [o+[num] for o in op]
    return op

print(subsets([1,2,3]))