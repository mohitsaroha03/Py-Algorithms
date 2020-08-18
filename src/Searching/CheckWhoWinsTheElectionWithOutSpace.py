# Link: 
# IsDone: 0
def CheckWhoWinsTheElection(A):
	A.sort()
	counter = maxCounter = 0
	candidate = maxCandidate = 0
	
	for i in range(0, len(A)):
		if(A[i] == candidate):
			counter += 1
		else:
			counter = 1
			candidate = A[i]

		if(counter > maxCounter):
			maxCandidate = A[i]
			maxCounter = counter

	print maxCandidate, "appeared ", maxCounter, " times"

		
A = [2, 3, 2, 1, 2, 2, 3, 2, 2]
CheckWhoWinsTheElection(A)
A = [3, 3, 3, 2, 2, 3]
CheckWhoWinsTheElection(A)
