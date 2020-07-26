# Link: 
# IsDone: 0
def twoElementsWithSumKWithHash(A, K):
	table = {}  # hash
	for element in A:
		if element in table:
			table[element] += 1
		elif element != " ":
			table[element] = 1
		else:
			table[element] = 0			
	for element in A:
		if K - element in table:
			print "yes-->", element, "+", K - element, " = ", K			
A = [1, 4, 45, 6, 10, -8]
A.sort()
twoElementsWithSumKWithHash(A, 11)
