
from collections import Counter

def scattered_pal(s):
    counts = Counter(s)
    print (len([count for count in counts.values() if count % 2 == 1]) <= 1)
    return counts

def scattered_palindrome(s):
    counts = Counter(s)
    return len([count for count in counts.values() if count % 2 == 1]) <= 1

print(scattered_palindrome("bbrrg"))