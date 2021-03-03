
'''
H3.3Write and test a Pythonfunction called cryptowhich will encrypt (and decrypt) text using a simple letter swap.
cryptois to be called with three parameters as crypto(x,n,enc),
where x will be a list of words (possibly with punctuation marks),
n will be an integer in the range 0 to 2,000,000,000,
and enc will be a Boolean value.
crypto will first seed the random number generator with n.
It will then create a random swap table for the letters of the alphabet.
For example‘a’ -> ‘w’‘b’ -> ‘d’‘c’ ->’a’‘d’-> ‘q’etc.
(Hint: the shuffle and/or permute functions in numpy.random might be useful here.)
If the value of enc is True, crypto should return a new list of words where each of the letters have been replaced with the letter from the given table, e.g. ‘bad’ would come out ‘dwq’ .
Capitals MUST follow the same replacement, e.g. ‘B’ would go to ‘D’.
Punctuation marks should be left unchanged. If encis False, crypto should reverse the substitution,
e.g., ‘awd’would be replaced with ‘cab’.
'''
import numpy as np
import string


def crypto(x, n, enc):
    # input

    # creates a random seed int from 0 to 2000,000,000
    random_seed_val = n
    np.random.seed(random_seed_val)

    # get a list of all alphabets
    letters = list(string.ascii_lowercase)

    # create a dictionary of alphabets in order
    d = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i',9:'j',10:'k',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'v',22:'w',23:'x',24:'y',25:'z'}

    # create a list of random numbers from 0 to 26 that'll be used to encrypt the alphabets using the above seed
    r = np.random.choice(np.arange(0, 26), replace=False, size=(1, 26))
    rand=r[0]

    # create a new dict for encryption
    newD = {}
    for i in range(26):
        letter= letters[i]
        newD[letter]=d[rand[i]]
    # create a third dict for decryption
    inv_newD = {v: k for k, v in newD.items()}

    newX = []

    # loop through the list of words and encrypt or decrypt based on "enc" value
    for word in x:
        newWord = ''
        for l in word:
            if enc is True:
                newWord+=newD[l]
            else:
                newWord+=inv_newD[l]
        print(newWord)
        newX.append(newWord)
    print(newX)

crypto(['abc','def','abcdefg','xyz'],2000000000,False)
