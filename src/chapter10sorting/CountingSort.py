''

def CountingSort(A, k):
	""" implementation of counting sort """
	B = [0 for el in A]
	C = [0 for el in range(0, k + 1)]

	for i in xrange(0, k + 1):
		C[i] = 0

	for j in xrange(0, len(A)):
		C[A[j]] += 1

	for i in xrange(1, k + 1):
		C[i] += C[i - 1]

	for j in xrange(len(A) - 1, 0 - 1, -1):
		tmp = A[j]
		tmp2 = C[tmp] - 1
		B[tmp2] = tmp
		C[tmp] -= 1
	return B
	
A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(CountingSort(A, 1000))

def counting_sort(A, k):
    """in-place counting sort"""
    n = len(A)
    m = k + 1
    C = [0] * m              
    for a in A:
        C[a] += 1           
    i = 0
    for a in range(m):            
        for c in range(C[a]): 
            A[i] = a
            i += 1
    return A

print counting_sort( [1, 4, 7, 2, 1, 3, 2, 1, 4, 2, 3, 2, 1], 7 )
