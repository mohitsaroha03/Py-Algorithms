# Link: 
# IsDone: 0
import math
def CheckDuplicatesNegationTechnique(A):
	for i in range(0, len(A)):
		if(A[abs(A[i])] < 0):
			print("Duplicates exist:", A[i])
			return
		else:
			A[abs(A[i])] *= -1
			
	print("No duplicates in given array.")

A = [3, 2, 1, 2, 2, 3]
CheckDuplicatesNegationTechnique(A)
