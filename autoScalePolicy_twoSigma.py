#hackerrank autoscale policy question - the question is in the Notes under Two sigma
import math
def finalinstances(inst,arr):
    isAction = False
    i=0
    while i < len(arr):
        if isAction:
            i=i+9
            isAction = False
            if i> len(arr):
                break
        else:
            if arr[i] < 25 and inst !=1:
                inst = math.ceil(inst/2)
                isAction = True
            elif arr[i] > 60:
                if(inst*2 < 2*(10**8)+1):
                    inst = inst * 2
                else:
                    return inst
                isAction = True
        i += 1

    return inst     

res = finalinstances(2,[25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80])   
print(res)            
