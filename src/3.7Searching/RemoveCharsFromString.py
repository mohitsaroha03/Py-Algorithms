# Link: 
# IsDone: 0
def RemoveChars(str, removeTheseChars):
	table = {}  # hash
	temp = []
	# set true for all characters to be removed
	for char in removeTheseChars.lower():
		table[char] = 1
	index = 0
	for char in str.lower():
		if char in table:
			continue
		else:
			temp.append(char)
			index += 1
	return "".join(temp)

print RemoveChars("careermonk", "e")

