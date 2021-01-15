######################################
#SLIIDING WINDOW
######################################

def slidingWindow(str,k):

#[80,-50,90,100] 
    n = len(str)
    window = sum([str[i] for i in range(0,k)])
    print(window)
    maxSum = window
    for i in range(0,n-k):
        window = window - str[i] + str[i+k]
        maxV = max(maxSum, window)

    print(maxV)

slidingWindow([80,-50,90,100],2)


######################################
# Alternate brute force way of solving the issue
######################################
# n = int(input("enter size of array"))
# arr = list(map(int, input().split()))


# def calcMaxSum(arr,n):
#     k = 2
#     maxSum = -0.0001
#     for i in range(0, n-k+1):
#         sumC = 0
#         for j in range(0, k):
#             sumC += arr[i+j]
#             maxSum = max(maxSum, sumC)
#     return maxSum


# ans = calcMaxSum(arr,n)
# print(ans)
