''

def findNonrepeated(A):
	n = len(A)
	for i in range(0, n):
		repeated = 0
		for j in range(0, n):
			if(i != j and A[i] == A[j]):
				repeated = 1
		if repeated == 0:
			return A[i]
	return
		
print findNonrepeated("careermonk")
