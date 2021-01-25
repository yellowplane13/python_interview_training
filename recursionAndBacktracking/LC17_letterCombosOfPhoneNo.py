def letterCombinations(digits):

    d = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    if not digits:
        return []
    sol = []
    currStr = ''

    findCombos_helperFn(digits, currStr, sol, d)
    return sol


def findCombos_helperFn(digits, currStr, sol, d):
    # base case in any recursion helper function
    if len(digits) == 0:
        sol.append(currStr)
        return

    for char in d[digits[0]]:
        currStr += char
        findCombos_helperFn(digits[1:], currStr, sol, d)
        currStr = currStr[:-1]

print(letterCombinations('23'))
#['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
