# isGFG: , Link: 
# IsDone: 0
def singleNumber(A):
	i = res = 0
 	for i in range (0, len(A)): 
		res = res ^ A[i]
	return res

A = [7, 3, 6, 3, 3, 6, 7	]
print singleNumber(A)
