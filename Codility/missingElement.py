
def solution(A):
    # write your code in Python 3.6
    # A 1 to N+1
    n = len(A)
    print('n',n)

    sumOfA = sum(A)
    print('sumOfA', sumOfA)
    N=n+1
    print('N',N)
    sumOfN = N*(N+1)//2
    print("sumOfN",sumOfN)
    diff = sumOfN - sumOfA
    print('diff',diff)

solution([2,3,5,1])