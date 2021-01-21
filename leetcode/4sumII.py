# class Solution(object):
#     def fourSumCount(self, A, B, C, D):
#         """
#         :type A: List[int]
#         :type B: List[int]
#         :type C: List[int]
#         :type D: List[int]
#         :rtype: int
#         """
#         hashtable = {}
#         for a in A:
#             for b in B :
#                 if a + b in hashtable :
#                     hashtable[a+b] += 1
#                 else :
#                     hashtable[a+b] = 1
#         count = 0         
#         for c in C :
#             for d in D :
#                 if -c - d in hashtable :
#                     count += hashtable[-c-d]
#         return count

class Solution:
    def fourSumCount(self, A, B, C, D):
        d = {}
        c = 0
        for a in A:
            for b in B:
                if a + b not in d:
                    d[a+b] = 1
                else:
                    d[a+b] += 1
        print (d)
        for k in range(len(C)):
            for l in range(len(D)):
                target = -(C[k] + D[l])
                if target in d:
                    print(target, "target")
                    print(C[k],D[l])
                    c += d[target]
                    print(c, 'c')
        return c
    
op = Solution()
op.fourSumCount([1,2],[-2,-1],[-1,2],[0,2])