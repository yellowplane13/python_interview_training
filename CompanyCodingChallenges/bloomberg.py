"""
   Object that tracks ints,
    First in, last out
    should also support retrieving the max int in the collection
    12, 14, 3, 2
    12, 14, 3, 2
    push(int)
    int pop()
    int getMax()
"""

stack = [ ]
# input arr
#arr = [12,14]
inputArr = [1,2,3,5,4,8,7,14]
maxarr = [1,2,3,5,5,8,8,14]

upperMax = 0

def pushStack(s):
    stack.append(s)
    upperMax = max(upperMax,s)
    maxarr.append(upperMax)
    
def popStack():
    stack.pop()
    maxarr.pop()
    upperMax = maxarr[-1]
    
def getMax():
    print(upperMax)
    
for a in inputArr:
    pushStack(a)
    
    #maxN = max(arr)
    
# def addNumbers(a,b):
#     sum = a + b
#     return sum

# num1 = int(input())
# num2 = int(input())

# print("The sum is", addNumbers(num1, num2))
