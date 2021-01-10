class Solution:
    def fizzbuzz(self, n):
        for i in range(1,n+1):
            if i % 15 == 0:
                print ("FizzBuzz")
            elif i % 3 == 0:
                print ("Fizz")
            elif i % 5 == 0:
                print ("Buzz")
            else:
                print (i)

sol = Solution()
sol.fizzbuzz(21)

#SOLUTION #2
# i=1
# while i <= 100:
#     if i%3==0:
#         print("Fizz", end="")
#         if i%5==0:
#             print("Buzz", end="")
#     elif i%5==0:
#         print("Buzz", end="")
#     else:
#         print(i, end="")
#     print()
#     i+=1
        