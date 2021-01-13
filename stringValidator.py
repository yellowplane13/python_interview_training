#########
#HACKERRANK
#SOLUTION 1
# if __name__ == '__main__':
#     s = 'qA2'
#     #print(any(sub.isalnum() for sub in s))
#     l = list(s)
#     an = []
#     a = []
#     d = []
#     lo = []
#     u = []
#     for sub in l:
#         an.append(sub.isalnum())
#         a.append(sub.isalpha())
#         d.append(sub.isdigit())
#         lo.append(sub.islower())
#         u.append(sub.isupper())
#     print(any(an))
#     print(any(a))
#     print(any(d))
#     print(any(lo))
#     print(any(u))

#SOLUTION 2
if __name__ == '__main__':
    s = input()
    print(any(sub.isalnum() for sub in s))
    print(any(sub.isalpha() for sub in s))
    print(any(sub.isdigit() for sub in s))
    print(any(sub.islower() for sub in s))
    print(any(sub.isupper() for sub in s))
    
    