# Link: 
# IsDone: 0
def rearrangeArrayElementsA1B1A2B2(A):
	n = len(A) // 2
	i = 0; 	q = 1; k = n
	while (i < n):
		
		j = k
		while j > i + q:
			A[j], A[j - 1] = A[j - 1], A[j]
			j -= 1
		i += 1; k += 1; q += 1

A = [1, 3, 5, 6, 2, 4, 6, 8]
rearrangeArrayElementsA1B1A2B2(A)
print A
