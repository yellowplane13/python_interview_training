# FIRST METHOD
arr = []
for i in range(int(input('enter the size of array:'))):
    arr.append(int(input()))
print (arr)
print (type(arr))

# SECOND METHOD
n = int(input("enter size of array"))
arr = list(map(int, input().split()))
print(type(arr))
print(arr)