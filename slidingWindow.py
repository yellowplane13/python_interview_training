import sys
# print (sys.argv)
n = int(input("enter size of array"))
arr = list(map(int, input().split()))
print(type(arr))
print(arr)

#arr = [80, -50, 90, 100]
#n = 4
k = 2
maxSum = -0.0001
for i in range(0,n-k+1):
    sumC = 0
    for j in range(0,k):
        sumC += arr[i+j]
        #print(sumC)
    maxSum = max(maxSum, sumC)
print(maxSum)