s = "46"
for i in range(5):
    print("i=",i)
    res = ""
    c = 1
    for j in range(len(s)):
        #print("j=",j)
        if j<len(s)-1:
            if s[j] != s[j+1]:
                res+= str(c) + s[j]
                c = 1
            else:
                c+=1
        else:
            c = 1
            res+= str(c) + s[j]
            c = 1
    s=res
    print("new S:",s)