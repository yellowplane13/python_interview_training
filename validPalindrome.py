###############
#680 LC Valid Palindrome II
class Solution:
    def isPal(self, s):
        self.s = s
        beg = 0
        end = len(s)-1
        for _ in range(len(s)):
                if s[beg] != s[end]:
                    return False
                beg += 1
                end -= 1
        return True

    def validPalindrome(self, s):
        n = len(s)
        beg = 0
        end = n-1
        if (n % 2 != 0):
            print(self.isPal(s))
        elif(n % 2 == 0):
            newS =[]
            for i in range(len(s)):
                if s[beg] != s[end]:
                    newS = s.replace(s[end], "")
                    break 
                beg += 1
                end -= 1
            print(self.isPal(newS))


                
            
op = Solution()
op.validPalindrome('abcdba')