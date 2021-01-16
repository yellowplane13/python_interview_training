
from collections import Counter

def scattered_palindrome(s):
    counts = Counter(s)
    print (len([count for count in counts.values() if count % 2 == 1]) <= 1)
    return counts

print(scattered_palindrome("aabb"))