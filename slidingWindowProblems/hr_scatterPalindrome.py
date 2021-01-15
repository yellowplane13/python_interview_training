# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         n = len(s)
#         c=0
#         for i in range(0,n-1): #i=0
#             print('i:',i)
#             for j in range(i+1,n+1): #j=1
#                 print('j',j)
#                 temp = s[i:j]
#                 if len(temp) == 1:
#                     c+=1
#                 # if the len of substring is even,
#                 # check if the reverse of the string is the same
#                 elif(len(temp)%2 == 0):
#                     if (temp == temp[::-1]):
#                         c+=1
#                         print("c",c)
#                 else:
#                     # create a dict to check for how many times
#                     # each value has occurred
#                     d = {}
#                     for l in range(len(temp)):
#                         if temp[l] in d:
#                             d[temp[l]] = d[temp[l]]+1
#                         else:
#                             d[temp[l]] = 1
#                     print(d)

#         return c
    
    
# op = Solution()
# op.countSubstrings('aabb')


from collections import Counter

def scattered_palindrome(s):
    counts = Counter(s)
    print (len([count for count in counts.values() if count % 2 == 1]) <= 1)
    return counts

print(scattered_palindrome("aabb"))