from typing import List
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        if not weight:
            return 0
        weight.sort()
        print(weight)
        count = 0
        totalW=0
        for i,v in enumerate(weight):
                totalW+=v
                if totalW>5000:
                    totalW=totalW-v
                    return count
                count+=1
                print(v)
                print(totalW)
        return count

    def maxNumberNotGood(self,weight):
        weight.sort()
        count=len(weight)
        sumT=sum(weight)
        while sumT > 5000:
            sumT=sumT-weight[-1]
            count-=1
        return count

op=Solution()
print(op.maxNumberOfApples([100,200,150,1000]))
print(op.maxNumberOfApples([900,950,800,1000,700,800]))
#print(op.maxNumberShortcut([900,950,800,1000,700,800]))



#next question to try: https://leetcode.com/problems/minimum-knight-moves/description/ 