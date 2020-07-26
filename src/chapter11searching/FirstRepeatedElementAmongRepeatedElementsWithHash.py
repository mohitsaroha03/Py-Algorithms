# Link: 
# IsDone: 0
def FirstRepeatedElementAmongRepeatedElementsWithHash(A):
	table = {}  # hash
	max = 0
	for element in A:
		if element in table and table[element] == 1:
			table[element] = -2
		elif element in table and table[element] < 0:
			table[element] -= 1			
		elif element != " ":
			table[element] = 1
		else:
			table[element] = 0

	for element in A:
		if table[element] < max:
			max = table[element]
			maxRepeatedElement = element

	print maxRepeatedElement, "repeated for ", abs(max), " times"
 
A = [3, 2, 1, 1, 2, 1, 2, 5, 5]
FirstRepeatedElementAmongRepeatedElementsWithHash(A)
