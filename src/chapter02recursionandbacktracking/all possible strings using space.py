# Link: https://www.geeksforgeeks.org/print-a-pattern-without-using-any-loop/
# IsDone: 1

# Python3 program to print pattern that 
# first reduces 5 one by one, then adds 5. 
# Without any loop an extra variable. 

# Recursive function to print the pattern 
# without any extra variable 
def printPattern(n): 

	# Base case (When n becomes 0 or negative) 
	if (n == 0 or n < 0): 
		print(n,) 
		return
	
	# First print decreasing order 
	print(n,) 
	printPattern(n - 5) 

	# Then print increasing order 
	print(n,) 

# Driver Code 
n = 16
printPattern(n) 
