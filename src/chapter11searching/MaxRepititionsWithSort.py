''

def MaxRepititionsWithSort(A):
	A.sort()
	print A
	j = 0
	count = max = 1
	element = A[0]
	for i in range(1, len(A)):
		if (A[i] == element):
			count += 1
			if count > max:
				max = count
				maxRepeatedElement = element
		else:
			count = 1
			element = A[i]
			
	print maxRepeatedElement, "repeated for ", max

A = [3, 2, 1, 3, 2, 3, 2, 3, 3]
MaxRepititionsWithSort(A)
