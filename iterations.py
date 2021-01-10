#print a right angle triangle
# for i in range(5):
#     for j in range(i):
#         print (' * ', end='')
#     print()

#print an isoceles triangle
n = 4
for i in range(n,0,-1):
    for k in range(n-i):
        print('   ', end='')
    for j in range(2*i - 1):
        print (' * ', end='')
    print()
    