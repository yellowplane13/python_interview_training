
n = int(input("enter size of array"))
arr = list(map(int, input().split()))


def calcMaxSum(arr,n):
    k = 2
    maxSum = -0.0001
    for i in range(0, n-k+1):
        sumC = 0
        for j in range(0, k):
            sumC += arr[i+j]
            maxSum = max(maxSum, sumC)
    return maxSum


ans = calcMaxSum(arr,n)
print(ans)
