#219 leetcode 

from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                    return True
            else:
                d[nums[i]] = i
                if len(d) > k:
                    del d[nums[abs(i-k)]]
                    
        return False

op = Solution()
print(op.containsNearbyDuplicate([1,2,3,1,2,3],2))