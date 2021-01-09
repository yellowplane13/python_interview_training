# # FIRST METHOD
# arr = []
# for i in range(int(input('enter the size of array:'))):
#     arr.append(int(input()))
# print (arr)
# print (type(arr))

# # SECOND METHOD
# n = int(input("enter size of array"))
# arr = list(map(int, input().split()))
# print(type(arr))
# print(arr)

# # THIRD METHOD
# n = int(input("enter size of array"))
# arr = list(map(int, input().split()))

import os
try:

    my_home = os.environ['MY_HOME']
    print(my_home)
except KeyError:
    print("It doesn't exist")

curr = os.getcwd
print(curr)