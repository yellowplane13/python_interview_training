import math
def solution(arr,k):
    a = [math.inf]*len(arr)
    for i in range(len(arr)):
        shift = (i+k) % len(arr)
        a[shift] = arr[i]
    print(a)
solution([3,2,6,0,7],4)
#####################
# The below method is O(N^2)
#####################
# def solution(arr,k):
#     if len(arr) == k:
#         return arr
#     else:
#         for i in range(0,k):
#             a = [0] * len(arr)
#             print("k:",i)
#             j=0
#             while j < len(arr)-1:
#                 a[j+1] = arr[j]
#                 j+=1
#             a[0] = arr[len(arr)-1]
#             arr = a
#             print(arr)
#     print(a)