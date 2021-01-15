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

a = 'book'
b = 'okbo'
dict = {}

for i in range(len(a)):
    if a[i] in dict:
        print(dict)
        dict[a[i]] = dict[a[i]] + 1 
    else:
        dict[a[i]] = 1
for i in range(len(b)):
    if b[i] in dict:
        dict[a[i]] -= 1
if sum(dict.values()) == 0:
    print(True)
else:
    print(False)