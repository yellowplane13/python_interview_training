# https://www.youtube.com/watch?v=IrD8MA054vA&ab_channel=TimothyHChang
class Solution: 
    def longestPalindrome(self, s: str) -> str:
        # for a given i, it checks to see if the left and right of the i are same letter
        def helper(l,r):
            while(l>=0 and r<len(s) and s[l] == s[r]):
                l-=1
                r+=1
            return s[l+1:r]

        # step 1 : for odd and even string, 
        # for every string in s, call the helper function to check if the left and right strings are equal
        # if equal, go further left and right of the array and check the same again
        # keep checking until left and right are not equal

        res = ''
        for i in range(len(s)):
            test = helper(i,i)
            if len(test) > len(res):
                res = test
                
            test = helper(i,i+1)
            if len(test) > len(res):
                res = test
        return res
    
op = Solution()

print(op.longestPalindrome('babad'))