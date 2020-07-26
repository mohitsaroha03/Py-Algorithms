# Link: 
# IsDone: 0
def findNonrepeated(A):
	table = {}  # hash
	for char in A.lower():
		if char in table:
			table[char] += 1
		elif char != " ":
			table[char] = 1
		else:
			table[char] = 0

	for char in A.lower():
		if table[char] == 1:
			print("the first non repeated character is: %s" % (char))
			return char

	return
 
print findNonrepeated("careermonk")
