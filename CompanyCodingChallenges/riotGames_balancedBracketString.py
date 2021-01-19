'''
Given a list of strings of bracket characters: {}(), the string of brackets is balanced under the following conditions:

It is the empty string.
If strings a and b are balanced, then ab is balanced.
If string a is balanced, then (a) and {a} are balanced.
Write a class that determines whether the brackets in each string are balanced and returns true if the string is balanced, or false if it is not.
Example 0
s = [ "{}()", "{()}", "({()})" ]
s[0] exhibits condition 2 above. "{}" and "()" are balanced, so "{}()" is balanced. Return true.

s[1] exhibits condition 3 above. "()" is balanced, so "{()}" is balanced. Return true.

s[2] exhibits condition 3 above. "()" is balanced, so "{()}" is balanced and "({()})" is balanced. Return true.


Example 1

s = ["{}(", "({)}", "((", "}{" ]
s[0] rarr 2. '"{}(" is an unbalanced string due to the open "(". Return false.

s[1] rarr 2. "({)}" is an unbalanced string due to ")" before "{" has been closed. Return false.

s[2] rarr 2. "((", is an unbalanced string because neither "(" is closed. Return false.

s[3] rarr 2. "}{" is an unbalanced string because "}" comes before a "{" and because the final "{" is not closed. Return false.

Function Description 

The provided code contains the declaration for a class named Solution with a main method that does the following:

Creates a Parser object.
Reads an unknown number of strings from stdin.
Passes each string as an argument to the Parser object's isBalanced method and prints value returned by the method on a new line.
 

Complete the function an isBalanced  in the editor below.

isBalanced has the following parameter(s):
   list<string>  s:  a list of strings of characters to check for balance

Returns :

    list<bool> : a list of corresponding booleans that denote whether the strings are balanced: true if the string is balanced, or false if it is not

Constraints
Each string consists only of the characters {, }, (, and ).
Each string has fewer than 50 characters.
Considerations:
What if we wanted to add more brace characters? How would we structure the code differently?
 
The first line will be an integer representing the total number of following test cases.

Each subsequent line contains a string to parse.

Sample Case 0
Sample Input 0

STDIN    Function 
-----    -------- 
3
{}()  →  s = ['{}())', '({()})', '{}(']
({()})
{}(
 

Sample Output 0

true
true
false
 

Explanation 0

2. '{}()' contains two adjacent balanced strings, '{} 'and '()', so return true.

3. '({()})' contains a balanced string, '()', nested inside another balanced string, '{}', nested inside another balanced string, '()'. Return true.

2. '{}(' contains a balanced string '{}', followed by an unbalanced string '('. Return false.

'''
#!/bin/python3

import math
import os
import random
import re
import sys
#
# The function is expected to return a BOOLEAN_ARRAY.
# The function accepts STRING_ARRAY braceStrings as parameter.
#

#This is what I wrote
def isBalancedTmp(Str):
    """
    :param Str: ["{}()", "{()}", "(})", "}"]
    s0 = "{}()"
    s1 = "{()}"
    """
    # Write your code here
    d = {
        "{":"}",
        "(":")"
    }
    
    if len(str) == 0:
        return True
    else:
    
        for s in Str: #{(})
            b = 0
            e = len(s)-1
            for i in range(s): #{
                if d[b] in s:
                    if s[e] == s[b]:
                        b += 1
                        e -= 1
                    else:
                        if s[b] == s[i+1]:
                            b += 1
                else:
                    return False
                
# This is what Tyler Turk wrote          
def isBalanced(braceStrings):
    d = {
        "{": "}",
        "(": ")"
    }
    results = []
    for braceString in braceStrings:
        stack = []
        for char in braceString:
            if char in d.keys():
                stack.append(d[char])
                continue
            elif char in d.values() and len(stack) > 0:
                if char == stack.pop():
                    continue
            stack = ["a"]
            break
        if not stack:
            results.append(True)
        else:
            results.append(False)
    return results
print(isBalanced(["{}(","({})","((","{}"]))
#["{}()","{()}", "({()})"]
#["{}(","({)}","((","{}"]

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     braceStrings_count = int(input().strip())

#     braceStrings = []

#     for _ in range(braceStrings_count):
#         braceStrings_item = input()
#         braceStrings.append(braceStrings_item)

#     result = ['true' if b else 'false' for b in isBalanced(braceStrings)]

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
