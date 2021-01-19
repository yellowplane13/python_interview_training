def shuffle(nums,n):
    ##### BORING WAY ######
        # arr1 = nums[:n]
        # arr2 = nums[n:]
        # op = []
        # for i in range(n):
        #     op.append(arr1[i])
        #     op.append(arr2[i])
        # return op
    ###### USING ZIP ########
    res = []
    for i,j in zip(nums[:n],nums[n:]):
        res += [i,j]
    return res

print(shuffle([2,5,1,3,4,7],3))