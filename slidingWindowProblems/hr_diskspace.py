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

def solution(x, space):
    arr = []
    minA = []
    for i in range(0,len(space)-x+1):
        print("i=", i)
        print("x-i=",x+i)
        print(space[1:3])
        arr.append(space[i:x+i])
        print("minA", min(arr[i]))
        print("arr[i]=",arr[i])
        minA.append(min(arr[i]))
    print(arr)
    print(minA)
    return max(minA)

op = solution(1, [1,2,3,1,2])
print(op)
