from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = {}
        for num in nums:
            if num in m:
                m[num] = m[num]+1
            else:
                m[num] = 1
        print("Dict:", m)
        print ("Max Key:", max(m))
        print("Max value: ", max(m.values()))
        return( max(m,key=m.get))

op = Solution()
print(op.majorityElement([2,2,2,1,1,1,2,2,70]))