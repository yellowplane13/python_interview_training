class Solution:
    def isPal(self, s, b, e):
        for i in range(n):
                if s[beg] != s[end]:
                    return False
                beg += 1
                end -= 1
        return True

    def validPalindrome(self, s):
        n = len(s)
        beg = 0
        end = n-1
        print(n%2)
        if (n % 2 != 0):
            op = isPal(s, beg, end)
        elif(n % 2 == 0):
            newS =[]
            for i in range(n):
                if s[beg] != s[end]:
                    newS = s.replace(s[end], '')
                    break 
                beg += 1
                end -= 1
            op = isPal(s, beg, end)


                
            
op = Solution()
op.validPalindrome('abcdba')