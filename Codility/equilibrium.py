import math
def solution(a):
    d = {}
    minDiff = math.inf 
    for i in range(1,len(a)):
        p = i
        temp1 = sum(a[0:p])
        temp2 = sum(a[p:len(a)])
        diff = abs(temp1 - temp2)
        d[p] = diff
        minDiff = min(minDiff, d[p])
        #sort the dictionary by values
        # you can't sort a dict , but you can create a list of tuples in sorted order

        ds = sorted(d.items(), key=lambda x: x[1])
    print(ds)
    print(minDiff)

solution([3,1,2,4,3])
