# Link: https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
# IsDone: 1

# Python program to print all permutations with 
# duplicates allowed 

def toString(List): 
	return ''.join(List) 

# Function to print permutations of string 
# This function takes three parameters: 
# 1. String 
# 2. Starting index of the string 
# 3. Ending index of the string. 
def permute(a, start, end): 
	if start==end: 
		print toString(a) 
	else: 
		for i in xrange(start,end+1): 
			a[start], a[i] = a[i], a[start] 
			permute(a, start+1, end) 
			a[start], a[i] = a[i], a[start] # backtrack 

# Driver program to test the above function 
string = "ABC"
n = len(string) 
a = list(string) 
permute(a, 0, n-1) 
