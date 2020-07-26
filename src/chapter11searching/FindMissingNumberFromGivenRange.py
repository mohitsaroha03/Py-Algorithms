# Link: 
# IsDone: 0
import sys
def findMissingNumberFromGivenRange(A, X, Y):
	n = len(A)
	S = [-sys.maxint] * (n)
	missingNum = -sys.maxint
	for i in range(0, n):
		S[A[i] - X] = A[i]
	for i in range(0, n):
		if(S[i] == -sys.maxint):
			missingNum = i + X
			break
	return missingNum		
A = [10, 16, 14, 12, 11, 10, 13 , 15, 17, 12, 19]
print findMissingNumberFromGivenRange(A, 10, 20)
