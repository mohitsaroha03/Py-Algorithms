# Link: https://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/
# Python3 program to find the row 
# with maximum number of 1s 

# Function to find the index 
# of first index of 1 in a 
# boolean array arr[] 
def first( arr, low, high): 
	if high >= low: 
		
		# Get the middle index 
		mid = low + (high - low)//2

		# Check if the element at 
		# middle index is first 1 
		if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1: 
			return mid 

		# If the element is 0, 
		# recur for right side 
		elif arr[mid] == 0: 
			return first(arr, (mid + 1), high) 
	
		# If element is not first 1, 
		# recur for left side 
		else: 
			return first(arr, low, (mid - 1)) 
	return -1

# Function that returns 
# index of row with maximum 
# number of 1s. 
def rowWithMax1s( mat): 
	
	# Initialize max values 
	R = len(mat) 
	C = len(mat[0]) 
	max_row_index = 0
	max = -1
	
	# Traverse for each row and 
	# count number of 1s by finding 
	# the index of first 1 
	for i in range(0, R): 
		index = first (mat[i], 0, C - 1) 
		if index != -1 and C - index > max: 
			max = C - index 
			max_row_index = i 

	return max_row_index 

# Driver Code 
mat = [[0, 0, 0, 1], 
	[0, 1, 1, 1], 
	[1, 1, 1, 1], 
	[0, 0, 0, 0]] 
print ("Index of row with maximum 1s is", 
	rowWithMax1s(mat)) 