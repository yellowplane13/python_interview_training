def indexOfMinimum(lst,index):      
    sublist = lst[index:]
    print (sublist)  
    for _ in lst:  
        minIndex = (min(sublist))  
        return minIndex  
print (indexOfMinimum([2,4,6,8,1,3,5,0,7,9], 4))