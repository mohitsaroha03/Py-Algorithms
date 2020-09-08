# Link: https://www.geeksforgeeks.org/camelcase-pattern-matching/
# IsDone: 0
# Python3 to find CamelCase Pattern 
# matching 
# TODO: https://practice.geeksforgeeks.org/problems/longest-palindromic-substring-in-linear-time/1
# Function that prints the camel 
# case pattern matching 
def CamelCase(words, pattern) : 

	# Map to store the hashing 
	# of each words with every 
	# uppercase letter found 
	map = dict.fromkeys(words,None); 

	# Traverse the words array 
	# that contains all the 
	# string 
	for i in range(len(words)) : 

		# Intialise str as 
		# empty 
		string = ""; 

		# length of string words[i] 
		l = len(words[i]); 
		for j in range(l) : 

			# For every uppercase 
			# letter found map 
			# that uppercase to 
			# original words 
			if (words[i][j] >= 'A' and words[i][j] <= 'Z') : 
				string += words[i][j]; 
				
				if string not in map : 
					map[string] = [words[i]] 
					
				elif map[string] is None : 
					map[string] = [words[i]] 
					
				else : 
					map[string].append(words[i]); 

	wordFound = False; 

	# Traverse the map for pattern 
	# matching 
	for key,value in map.items() : 

		# If pattern matches then 
		# print the corresponding 
		# mapped words 
		if (key == pattern) : 
			wordFound = True; 
			for itt in value : 
				print(itt); 

	# If word not found print 
	# "No match found" 
	if (not wordFound) : 
		print("No match found"); 


# Driver's Code 
if __name__ == "__main__" : 

	words = [ 
		"Hi", "Hello", "HelloWorld", 
		"HiTech", "HiGeek", "HiTechWorld", 
		"HiTechCity", "HiTechLab"
	]; 

	# Pattern to be found 
	pattern = "HT"; 

	# Function call to find the 
	# words that match to the 
	# given pattern 
	CamelCase(words, pattern); 