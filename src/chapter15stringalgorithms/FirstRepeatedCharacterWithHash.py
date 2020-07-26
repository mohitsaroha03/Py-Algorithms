# Link: 
# IsDone: 0
def firstRepeatedChar(A):
	table = {}  # hash
	for char in A.lower():
		if char in table:
			table[char] += 1
			print("the first repeated character is: %s" % (char))
			return char
		elif char != " ":
			table[char] = 1
		else:
			table[char] = 0
	return

print firstRepeatedChar("careermonk")
