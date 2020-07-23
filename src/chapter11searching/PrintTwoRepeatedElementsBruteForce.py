# isGFG: , Link: 
# IsDone: 0
  
def PrintTwoRepeatedElementsBruteForce(A):
	n = len(A)
	for i in range(0, n):
		for j in range(i + 1, n):
			if(A[i] == A[j]):
				print A[i]


A = [3, 5, 7, 4, 2, 4, 2, 1, 9]
PrintTwoRepeatedElementsBruteForce(A)
