''

def checkPairwiseSorted(A):
	n = len(A)
	if (n == 0 or n == 1):
		return 1
	for i in range(0, n - 1, 2):	
		if (A[i] > A[i + 1]):
			return 0
	return 1


A = [34, 48, 10, 13, 2, 80, 30, 23]
print checkPairwiseSorted(A)
