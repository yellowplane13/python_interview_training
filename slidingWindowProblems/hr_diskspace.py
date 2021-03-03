# A company is performing an analysis on the computers at its main office. The computers are spaced along a single row. The analysis is performed in the following way:

# 1. Choose a contiguous segment of a certain number of computers, starting from the beginning of the row.
# 2. Analyze the available hard disk space on each of the computers.
# 3. Determine the minimum available disk space within this segment.

# After performing these steps for the first segment, it is then repeated for the next segment, continuing this procedure until the end of the row (i.e if the segment is 4, computers 1 to 4 would be analyzed, then 2 to 5, etc...) Given this analysis procedure, find the maximum available disk space among all the minima that are found during analysis

# Example
# n = 3, the number of computers
# space = [8, 2, 4]
# x = 2, the length of analysis segments

# In this array of computers, the subarrays of size 2 are [8, 2] and [2, 4]. Thus, the initial analysis returns 2 and 2 because those are the minima for the segments. Finally, the maximum of these values is 2. Therefore, the answer is 2.

# def solution(x, space):
#     arr = []
#     minA = []
#     for i in range(0,len(space)-x+1):
#         arr.append(space[i:x+i])
#         minA.append(min(arr[i]))
#     return max(minA)

# op = solution(1, [1,2,3,1,2])
# print(op)

def segment(x,space):
    tempI=[]
    n=len(space)
    maxOfMinArr=0

    for i in range(x):
        while len(tempI)!=0 and (space[i] <= space[tempI[-1]]):
                tempI.pop()
        tempI.append(i)
    for i in range(x, n):
        # simulaneously figure of the max of current window and the previous window
        maxOfMinArr=max(maxOfMinArr,space[tempI[0]])
        while len(tempI)!=0 and tempI[0] <= i-x:
            tempI.pop(0)
        # compare s[i] with its previous value. and store the i for the smallest value
        while len(tempI)!=0 and space[i] <= space[tempI[-1]] :
            tempI.pop()
        tempI.append(i)
    maxOfMinArr=max(maxOfMinArr,space[tempI[0]])
    return maxOfMinArr
op = segment(2, [1,2,3,1,2])
print(op)

# def segment(x,space):
#     n=len(space)
#     l=[]
#     ans=0
#     # Process first first window
#     # elements of space list
#     for i in range(x):
       
#         # For every element, the previous
#         # greater elements are useless
#         # so remove them from list
#         while len(l)!=0 and space[i] <= space[l[-1]]:
#                 l.pop()
         
#         # Add new element at last of list
#         l.append(i);
         
#     # Process the space[x] to
#     # space[n-1] elements
#     for i in range(x, n):
         
#         # The element at the front of the
#         # dequeue is the smallest element of
#         # previous window
#         ans=max(ans,space[l[0]])
         
#         # Remove the elements which are
#         # out of this window
#         while len(l)!=0 and l[0] <= i-x:
             
#             # remove from front of list
#             l.pop(0)
         
#         # Remove all elements greater than
#         # the currently being added element
#         while len(l)!=0 and space[i] <= space[l[-1]] :
#             l.pop()
         
#         # Add current element at the last of list
#         l.append(i)
   
   
