''

import random

def kthSmallest(data, k):
    "Find the nth rank ordered element (the least value has rank 0)."
    data = list(data)
    if not 0 <= k < len(data):
        raise ValueError('not enough elements for the given rank')
    while True:
        pivot = random.choice(data)
        pcount = 0
        under, over = [], []
        uappend, oappend = under.append, over.append
        for elem in data:
            if elem < pivot:
                uappend(elem)
            elif elem > pivot:
                oappend(elem)
            else:
                pcount += 1
        if k < len(under):
            data = under
        elif k < len(under) + pcount:
            return pivot
        else:
            data = over
            k -= len(under) + pcount
	
print(kthSmallest([2, 1, 5, 234, 3, 44, 7, 6, 4, 5, 9, 11, 12, 14, 13], 5))
