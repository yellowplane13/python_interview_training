#49
class Solution:
    
    def groupAnagrams(self, strs): 
        d = {}
        for s in strs:
            # when you sort a str, it puts it in an array... 
            # so join it back and add it to dup
            dup = "".join(sorted(s))
            # for multiple values of sorted(s) -> dup, append it to the array 
            # created for every key in the dict d
            if dup in d:
                d[dup].append(s)
                #print(d[dup])
            else:
                d[dup] = []
                d[dup].append(s)
                
        # iterate over the values to print the list of values to another list
        op = []
        for k,v in d.items():
            op.append(v)
        return op
    
sol = Solution()
output = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(output)