def solution(n,k):
    N = [0]* n
    for i in range(0,n):
        if k[i] > n:
            maxCounter(N,n)
        else:
            N[k[i]] +=1
    print (N)

def maxCounter(N,n):
    maxN = max(N)
    N = [0] * n
    N = [N[i]=maxN for i in range(n)]
    return N

solution(5,[3,4,4,6,1,4,4])