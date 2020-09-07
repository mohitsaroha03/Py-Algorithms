# Link: 
# IsDone: 0
def MaxRepititionsWithHash(A):
	table = {}  # hash
	max = 0
	for element in A:
		if element in table:
			table[element] += 1
		elif element != " ":
			table[element] = 1
		else:
			table[element] = 0

	for element in A:
		if table[element] > max:
			max = table[element]
			maxRepeatedElement = element

	print maxRepeatedElement, "repeated for ", max, " times"
 
A = [3, 2, 1, 3, 2, 3, 2, 3, 3]
MaxRepititionsWithHash(A)
