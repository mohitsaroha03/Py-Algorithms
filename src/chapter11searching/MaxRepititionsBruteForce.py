''

def MaxRepititionsBruteForce(A):
	n = len(A)
	count = max = 0
	for i in range(0, n):
		count = 1
		for j in range(0, n):
			if(i != j and A[i] == A[j]):
				count += 1
		if max < count:
			max = count
			maxRepeatedElement = A[i]
	print maxRepeatedElement, "repeated for ", max

A = [3, 2, 1, 2, 2, 3, 2, 1, 3]
MaxRepititionsBruteForce(A)
