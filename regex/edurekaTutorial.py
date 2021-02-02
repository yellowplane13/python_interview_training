import re
 
# Nameage = 'Hey this is the: b-staart of 123'
# # Janice is 22 and Theon is 33
# # Gabriel is 44 and Joey is 21
# # '''
# ages = re.findall(r'd\b', Nameage)
# #ages = re.compile(r'd', Nameage)
# print(ages)
# #names = re.

import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))


# ages = re.findall(r'd{1,3}', Nameage)
# names = re.findall(r'[A-Z][a-z]*',Nameage)
 
# ageDict = {}
# x = 0
# for eachname in names
#     ageDict[eachname] = ages[x]
#     x+=1
# print(ageDict)

# my_string = 'abc123ABC123abc'
# pattern = re.compile(r'abc')
# matches = pattern.finditer(my_string)
# for match in matches:
#     print(match)