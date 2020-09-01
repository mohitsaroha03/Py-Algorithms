# Link: 
# IsDone: 0
def CheckWhoWinsTheElection(A):
	counter = maxCounter = 0
	candidate = A[0]
	for i in range(0, len(A)):
		counter = 1
		for j in range(i + 1, len(A)):
			if(A[i] == A[j]): 
				counter += 1		
		if(counter > maxCounter):
			maxCounter = counter
			candidate = A[i]	
	print (candidate, "appeared ", maxCounter, " times")

A = [3, 2, 1, 2, 2, 3]
CheckWhoWinsTheElection(A)
A = [3, 3, 3, 2, 2, 3]
CheckWhoWinsTheElection(A)
