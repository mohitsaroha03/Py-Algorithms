''

def linear_search_count(A, data):
	count = 0
	for i in range (0, len(A)): 
		if(A[i] == data):
			count += 1
	return count

A = [7, 3, 6, 3, 3, 6, 7	]
print linear_search_count(A, 7)
