# isGFG: , Link: 
# IsDone: 0
def frequencyCounter(A):
	table = {}  # hash
	for element in A:
		if element in table:
			table[element] += 1
		elif element != " ":
			table[element] = 1
		else:
			table[element] = 0
	for element in A:
		print element, "--->", table[element]
 
A = [10, 1, 9, 4, 7, 6, 5, 22, 13, 2, 1]
frequencyCounter(A)
