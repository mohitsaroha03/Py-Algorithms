# Link: https://www.geeksforgeeks.org/maximum-absolute-difference-value-index-sums/
# Brute force Python 3 program 
# to calculate the maximum 
# absolute difference of an array. 

def calculateDiff(i, j, arr): 

	# Utility function to calculate 
	# the value of absolute difference 
	# for the pair (i, j). 
	return abs(arr[i] - arr[j]) + abs(i - j) 

# Function to return maximum 
# absolute difference in 
# brute force. 
def maxDistance(arr, n): 
	
	# Variable for storing the 
	# maximum absolute distance 
	# throughout the traversal 
	# of loops. 
	result = 0

	# Iterate through all pairs. 
	for i in range(0,n): 
		for j in range(i, n): 

			# If the absolute difference of 
			# current pair (i, j) is greater 
			# than the maximum difference 
			# calculated till now, update 
			# the value of result. 
			if (calculateDiff(i, j, arr) > result): 
				result = calculateDiff(i, j, arr) 
		
	return result 

# Driver program 
arr = [ -70, -64, -6, -56, 64, 
		61, -57, 16, 48, -98 ] 
n = len(arr) 

print(maxDistance(arr, n)) 