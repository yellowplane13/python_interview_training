class Solution:
    def numRescueBoats(self, p, limit):
        b = 0
        beg = 0
        end = len(p)-1
        print(p)
        p.sort()
        print(p)
        
        while beg <= end:
            if (beg == end):
                b += 1
                break
            if (p[beg] + p[end] <= limit):
                print("I'm in less loop")
                b += 1
                beg += 1
                end -= 1
            else:
                end -= 1
                b += 1
            
        return b

sol = Solution()
result = sol.numRescueBoats([7,8], 8)
print(result)