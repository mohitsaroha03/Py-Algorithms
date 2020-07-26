# Link: 
# IsDone: 0
def PrintTwoRepeatedElementsHash2(A):
	table = {}  # hash
	for element in A:
		# print element
		if element in table and table[element] == 1:
			print element
			table[element] += 1
		elif element in table:
			table[element] += 1	
		elif element != " ":
			table[element] = 1
		else:
			table[element] = 0
A = [3, 5, 7, 4, 2, 4, 2, 1, 9]
PrintTwoRepeatedElementsHash2(A)
