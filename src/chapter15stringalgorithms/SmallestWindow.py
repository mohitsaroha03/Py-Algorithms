''

from collections import defaultdict

def smallestWindow(INPUT, CHARS):
    assert CHARS != ''
    disctionary = defaultdict(int)
    nneg = [0]  # number of negative entries in dictionary
    def incr(c):
        disctionary[c] += 1
        if disctionary[c] == 0:
            nneg[0] -= 1
    def decr(c):
        if disctionary[c] == 0:
            nneg[0] += 1
        disctionary[c] -= 1
    for c in CHARS:
        decr(c)
    minLength = len(INPUT) + 1
    j = 0
    for i in xrange(len(INPUT)):
        while nneg[0] > 0:
            if j >= len(INPUT):
                return minLength
            incr(INPUT[j])
            j += 1
        minLength = min(minLength, j - i)
        decr(INPUT[i])
    return minLength
    
print  smallestWindow("ADOBECODEBANC", "ABC")
