class Solution:
    def merge(self, intervals):
        # step 1 ; sort
        intervals.sort()
        res = []
        
        for interval in intervals:
            # if res is null or if the last item's last value appeded to res 
            # is less than inverval's first val
            # eg: res = [1,3] so res[-1][1] = 3 which is gt than interval's                 # first val 2 ... 3 < 2, so don't append
            if (res == [] or res[-1][1] < interval[0]):
                res.append(interval)
            else:
                # find the max value between the two interval[1] -->
                #[1,3] and [2,6] for example
                maxVal = max(res[-1][1],interval[1])
                res[-1][1] = maxVal
        return res
                