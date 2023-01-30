# def solution(X):
#     # Implement your solution here
#     while True:
#         a,b=0,1
#         l,r=0,0

#         nextInt=a+b
#         a=b
#         b=nextInt

#         if (b<X):
#             l=b
#         else:
#             r=b
#             break
#     if X-l < r-X:
#         return X-l
#     else:
#         return r-X

# print(solution(13))

# write a function that given an integer x, returns an integer that corresponds to the minimum number of steps required to change x to a fibonnachi number 
# Here is a Python function that takes in an integer x and returns the minimum number of steps required to change it to a Fibonacci number:


def min_steps_to_fib(x):
    fib = [0, 1]  # Initialize list with first 2 Fibonacci numbers
    while fib[-1] < x:
        fib.append(fib[-1] + fib[-2])  # Generate next Fibonacci number
    steps = 0
    for num in fib:
        if num == x:
            return steps  # If x is already a Fibonacci number, return 0
        steps += 1
    return float('inf')  # If x is greater than the highest Fibonacci number, return infinity
# This function first generates a list of all Fibonacci numbers less than or equal to x using a while loop. 
# Then, it iterates through the list and checks if x is equal to any of the Fibonacci numbers. 
# If it is, the function returns the number of steps required to reach that Fibonacci number 
# (which is 0 since it is already a Fibonacci number). 
# If x is not in the list of Fibonacci numbers, the function returns infinity.