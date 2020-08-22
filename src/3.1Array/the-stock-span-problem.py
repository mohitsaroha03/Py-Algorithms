# Link: https://www.geeksforgeeks.org/the-stock-span-problem/
# Python3 program for a linear time 
# solution for stock span problem 
# without using stack 

# An efficient method to calculate 
# stock span values implementing 
# the same idea without using stack 
def calculateSpan(A, n, ans): 
	
	# Span value of first element 
	# is always 1 
	ans[0] = 1

	# Calculate span values for rest 
	# of the elements 
	for i in range(1, n): 
		counter = 1
		
		while ((i - counter) >= 0 and
			A[i] >= A[i - counter]): 
			counter += ans[i - counter] 
		ans[i] = counter 

# A utility function to print elements 
# of array 
def printArray(arr, n): 
	
	for i in range(n): 
		print(arr[i], end = ' ') 
	print() 

# Driver code 
price = [ 10, 4, 5, 90, 120, 80 ] 
n = len(price) 
S = [0] * (n) 

# Fill the span values in array S[] 
calculateSpan(price, n, S) 

# Print the calculated span values 
printArray(S, n) 