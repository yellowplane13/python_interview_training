#https://www.youtube.com/watch?v=pcPFrFK-ZVk&ab_channel=TimothyHChang
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rb = 0 # row beginning
        re = len(matrix) # row end
        cb = 0 # column beginning
        ce = len(matrix[0]) #column end
        res = []
        while rb < re and cb < ce:
            #right
            if rb < re:
                res += [matrix[rb][i] for i in range(cb,ce)]
                print(res,":right")
            rb+=1
            
            #down
            if cb < ce:
                res += [matrix[j][ce-1] for j in range(rb,re)] # rb = 1 re = 2 cb = 0 ce = 2
            print(res,":down")
            ce -= 1
            
            # left
            if rb < re:
                res += [matrix[re-1][k] for k in range(ce-1,cb-1,-1)]
            # rb = 1 re = 2 cb = 0 ce = 1
            print(res,":left")
            re-=1
            
            #up
            if cb < ce:
                res += [matrix[l][cb] for l in range(re-1,rb-1,-1)]
            # rb = 1 re = 1 cb = 0 ce = 1
            cb+=1
            print(res,":up")
            
            print(f"rb:{rb},re:{re},cb:{cb},ce:{ce}")
        return res

op = Solution()
print(op.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(op.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))