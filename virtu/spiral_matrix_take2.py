#https://www.youtube.com/watch?v=pcPFrFK-ZVk&ab_channel=TimothyHChang
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while len(matrix) != 0 and len(matrix[0]) != 0:
                res += matrix[0]
                del matrix[0]
                print(matrix)
                for i in matrix:
                    print ("i[-1]",i[-1])
                    res.append(i[-1])
                
                for i in range(len(matrix)):
                    del matrix[i][-1] 
                    print(matrix)
                
                if len(matrix) != 0 and len(matrix[0]) != 0:
                    res += matrix[-1][::-1]
                    del matrix[-1]   
                    print(matrix)
                    res += list(reversed([i[0] for i in matrix]))
                    for i in range(len(matrix)):
                        del matrix[i][0] 
                        print(matrix)
        return res


op = Solution()
print(op.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))