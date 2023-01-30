from typing import List
class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        existingWt=weight[0]
        remainingWt=5000-existingWt
        print(remainingWt)

        weight.pop(0)
        #weight.sort()
        print(weight)
        count = 0
        totalW=0
        for i,v in enumerate(weight):
                totalW+=v
                if totalW>remainingWt:
                    totalW=totalW-v
                    return count
                count+=1
                print(v)
                print(totalW)
        return count

    # def maxNumberNotGood(self,weight):
    #     weight.sort()
    #     count=len(weight)
    #     sumT=sum(weight)
    #     while sumT > 5000:
    #         sumT=sumT-weight[-1]
    #         count-=1
    #     return count

op=Solution()
#print(op.maxNumberOfApples([100,200,150,1000]))
#print(op.maxNumberOfApples([900,950,800,1000,700,800]))
#print(op.maxNumberShortcut([900,950,800,1000,700,800]))
print(op.maxNumberOfApples([4850,100,30,30,100,50,100]))




#next question to try: https://leetcode.com/problems/minimum-knight-moves/description/ 