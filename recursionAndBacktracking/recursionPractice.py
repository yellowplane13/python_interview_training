dig = '234567890'
#while len(dig) >0:
 #   dig = dig[:-1]
 #   print(dig)


def reduceDigits(digits):
    print(digits)
    if not digits:
        print("all done")
        return
    digits = reduceDigits(digits[:-1])
    

reduceDigits(dig)   