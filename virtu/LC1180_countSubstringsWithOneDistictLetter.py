# class Solution:
#     def countLetters(self, s) -> int:
#         count=0
#         substr=[]
#         i=0
#         for i in range(len(s)-2):
#             p1=i
#             p2=i+1
#             while p2<len(s) and s[p1]==s[p2]:
#                 substr.append(s[p1])
#                 substr.append(s[p2])
#                 print("substr",substr)
#                 p2+=1
#                 print("i2",i)
#                 count+=1
#             else:
#                 count+=1
#             i+=1
#         count+=len(substr)*(len(substr)+1)//2
#         return count

# op=Solution()
# print(op.countLetters("aaaba"))

##############################
def countLetters(self, S: str) -> int:
        res = 0
        same_count = 1
        for i, c in enumerate(S):
            if i > 0:
                if S[i - 1] == c:
                    same_count += 1
                else:
                    same_count = 1
            res += same_count
        
        return res