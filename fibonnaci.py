# Fibonacci using recursion and hashmaps
fibMap= {}
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        if n in fibMap:
            return fibMap[n]
        else:
            res = fib(n-1) + fib(n-2)
            fibMap[n] = res
    return res

def fibArray(n):
    fibarr = []
    for i in range(n):
        fibarr.append(fib(i))
    print(fibarr)

fibArray(16)
