def kidsWithCandies(candies, extra):
    maxN = max(candies)
    res = [True if(maxN - i) <= extra else False for i in candies]
    return res


print(kidsWithCandies([2, 3, 5, 1, 3], 3))