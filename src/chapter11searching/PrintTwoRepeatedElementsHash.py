# Link: 
# IsDone: 0
def PrintTwoRepeatedElementsHash(A):
	table = {}  # hash
	for element in A:
		if element in table:
			table[element] += 1
		elif element != " ":
			table[element] = 1
		else:
			table[element] = 0

	for element in A:
		if table[element] == 2:
			print element
			
A = [3, 5, 7, 4, 2, 4, 2, 1, 9]
PrintTwoRepeatedElementsHash(A)
