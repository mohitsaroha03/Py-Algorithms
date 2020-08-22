# Link: https://www.geeksforgeeks.org/largest-subset-whose-all-elements-are-fibonacci-numbers/
# python3 program to find largest Fibonacci subset 

# Prints largest subset of an array whose 
# all elements are fibonacci numbers 
def findFibSubset(arr, n): 

	# Find maximum element in arr[] 
	m= max(arr) 

	# Generate all Fibonacci numbers till 
	# max and store them in hash. 
	a = 0
	b = 1
	hash = [] 
	hash.append(a) 
	hash.append(b) 
	while (b < m): 
	
		c = a + b 
		a = b 
		b = c 
		hash.append(b) 
	

	# Npw iterate through all numbers and 
	# quickly check for Fibonacci using 
	# hash. 
	for i in range (n): 
		if arr[i] in hash : 
			print( arr[i],end=" ") 

# Driver code 
if __name__ == "__main__": 

	arr = [4, 2, 8, 5, 20, 1, 40, 13, 23] 
	n = len(arr) 
	findFibSubset(arr, n) 
