def twoSum(nums,t):
    d = {}
    for i in range(len(nums)):
        print ("num", nums[i])
        if nums[i] not in d:
            # store the difference as key and the index of i as value
            d[t-nums[i]] = i
            print("d",d)
        else:
            return d[nums[i]],i

print(twoSum([3,6,14,12], 15))
