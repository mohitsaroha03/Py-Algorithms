''

def RemoveDuplicates(A):
    m = 0
    for i in range(0, len(A)):
        if (not elem(A, m, A[i])):
            A[m] = A[i]
	    m += 1 
    return m

def elem(A, n, e):
    for i in range(0, n):
        if (A[i] == e):
            return 1 
    return 0

A = [54, 26, 93, 54, 77, 31, 44, 55, 20]
RemoveDuplicates(A)
print A
