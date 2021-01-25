dig = '234567890'
# without recursion
#while len(dig) >0:
 #   dig = dig[:-1]
 #   print(dig)
def reduceDigits(digits):
    print(digits)
    if not digits:
        print("all done")
        return
    reduceDigits(digits[:-1])
    

reduceDigits(dig)   