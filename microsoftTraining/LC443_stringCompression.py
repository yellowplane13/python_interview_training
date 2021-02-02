#
#
#["a","a","b","b","c","c","c"]
#      i
#          j
# if chars(j) != chars(j-1) then i++ and replace chars(i) with the count value
from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        c = 1
        i = 0
        for j in range(1,len(chars)+1):
            if j < len(chars) and chars[j] == chars[j-1]:
                c+=1
            else:
                chars[i] = chars[j-1]
                i+=1
                if c > 1:
                    
                    for k in str(c):
                        chars[i]=k
                        i+=1
                # reset c to 1 everytime a new char is found
                c = 1
        chars = chars[:i]
        print(chars)
        return len(chars)
# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         c = 1
#         i = 0
#         for j in range(1, len(chars)+1):
#             if j < len(chars) and chars[j] == chars[j-1]:
#                 c +=1
#             else:
#                 chars[i] = chars[j-1]
#                 chars[i] = c
#                 c = 1
#                 i+=1
               
#         return chars
            
# # ["a","a","b","b","c","c","c"]

# class Solution:
#     def compress(self, chars: List[str]) -> int:
#         c = 1
#         i = 0
#         j = 0
#         while i < len(chars):
#             c = 0
#             d = {}
#             while j < len(chars):
#                 if chars[i] == chars[j]:
#                     c+=1
#                     j+=1
#                 else:
#                     chars[i+1]=c
#                     i=j
#         print(chars)
            
# # ["a","a","b","b","c","c","c"]