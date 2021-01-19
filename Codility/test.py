def solution(A):
    # write your code in Python 3.6
    sumA = 0
    for i in A:
        if 9 < abs(i) <100:
            sumA += i

    return sumA

print(solution([-10,-12,-67,-9]))
