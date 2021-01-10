# def isAnagram(s1, s2):
#     if (len(s1) != len(s2)):
#         return False

#     compMap = {}

#     for i in range(len(s1)):
        
#         compMap[s1[i]] = compMap[s1[i]] + 1
#         print(compMap[s1[i]])
#         compMap[s2[i]] = compMap[s2[i]] - 1

#     for k,v in compMap:
#         if (v == 0):
#             return False

#     return True

# isAnagram('book', 'okbo')

s1 = 'book'
s2 = 'okbo'
dict = {}

for i in range(len(s1)):
    if s1[i] in dict:
        dict[s1[i]] = dict[s1[i]] + 1
    else:
        dict[s1[i]] = 1
for i in range(len(s2)):
    if s2[i] in dict:
        dict[s1[i]] -= 1
if sum(dict.values()) == 0:
    print(True)
else:
    print(False)