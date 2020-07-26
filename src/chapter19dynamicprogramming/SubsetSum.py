# Link: 
# IsDone: 0
def positiveSubsetSum(A, X):
	# preliminary
	if X < 0 or X > sum(A):  # T = sum(A)
		return False

	# algorithm
	subSum = [False] * (X + 1)
	subSum[0] = True
	p = 0
	while not subSum[X] and p < len(A):
		a = A[p]
		q = X
		while not subSum[X] and q >= a:
			if not subSum[q] and subSum[q - a]:
				subSum[q] = True
			q -= 1
		p += 1
	return subSum[X]
