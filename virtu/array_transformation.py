class Solution:
    def transformArray(self, arr:list) -> list:
        for i in range(len(arr)):
            print ("i", i)
            res = []
            for j, num in enumerate(arr):
                if j!=0 and j!=(len(arr)-1):
                    if num > arr[j-1] and num > arr[j+1]:
                        res.append(num-1)
                    elif num < arr[j-1] and num < arr[j+1]:
                        res.append(num+1)
                    else:
                        res.append(num)
                else:
                    res.append(num)
            if arr != res:
                arr = res
            else:
                break
        return res

op = Solution()
result=op.transformArray([1,9,7,4,8,9])
#result=op.transformArray([1,6,7,4,8,5])
result=op.transformArray([1,6,3,4,3,5])
print(result)
#next problem to sovle : https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/ 