# isGFG: , Link: 
# IsDone: 0
def MaxContigousSum(A):
	sumSoFar = sumEndingHere = 0
	n = len(A)
	for i in range(0, n) :
		sumEndingHere = sumEndingHere + A[i]
		if(sumEndingHere < 0):
			sumEndingHere = 0
			continue
		if(sumSoFar < sumEndingHere):
			sumSoFar = sumEndingHere

	return sumSoFar


A = [-2, 3, -16, 100, -4, 5]
print MaxContigousSum(A)
A = [-2, 11, -4, 13, -5, 2 ]
print MaxContigousSum(A)
A = [-15, -23, -476, -3, -292]
print MaxContigousSum(A)
