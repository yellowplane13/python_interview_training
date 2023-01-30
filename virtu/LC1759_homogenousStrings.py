class Solution:
    def countHomogenous(self, s: str) -> int:
        
        l = len(s)
        blockLen = 0
        res = 0
        
        def numOfHomoSubs(blockLen):
            return blockLen * (blockLen + 1) // 2
        
        for i in range(l):
            blockLen += 1
            if(i == l - 1 or s[i] != s[i+1]):
                res += numOfHomoSubs(blockLen)
                blockLen = 0
                
        return res % (10 ** 9 + 7) 

op=Solution()
#print(op.countHomogenous("abbcccaa"))
print(op.countHomogenous("c"))