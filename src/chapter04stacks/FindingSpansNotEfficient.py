''

def findingSpans(A):
	s = [None] * len(A)
	for i in range(0, len(A)):
		j = 1					
		while j <= i and A[i] > A[i - j]:
		       j = j + 1			                     
		s[i] = j	    		 	
	print s

findingSpans(['6', '3', '4', '5', '2'])
