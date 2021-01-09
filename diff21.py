def diff21(n):
  if (n < 21):
    return (abs(21 - n))
  else:
    num = (n - 21)
    return (abs(num**2))


res = diff21(25)
print("Result of def21 function is {}".format(res))