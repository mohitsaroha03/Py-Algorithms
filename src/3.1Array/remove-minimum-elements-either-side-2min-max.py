# Link: https://www.geeksforgeeks.org/remove-minimum-elements-either-side-2min-max/
# A O(n*n) solution to find the minimum of 
# elements to be removed 
import sys; 

# Returns the minimum number of removals 
# from either end in arr[l..h] so that 
# 2*min becomes greater than max. 
def minRemovalsDP(arr, n): 

	# Initialize starting and ending indexes 
	# of the maximum sized subarray 
	# with property 2*min > max 
	longest_start = -1; 
	longest_end = 0; 

	# Choose different elements as starting point 
	for start in range(n): 
		
		# Initialize min and max 
		# for the current start 
		min = sys.maxsize; 
		max = -sys.maxsize; 

		# Choose different ending points for current start 
		for end in range(start,n): 
			# Update min and max if necessary 
			val = arr[end]; 
			if (val < min): 
				min = val; 
			if (val > max): 
				max = val; 

			# If the property is violated, then no 
			# point to continue for a bigger array 
			if (2 * min <= max): 
				break; 

			# Update longest_start and longest_end if needed 
			if (end - start > longest_end - longest_start or longest_start == -1): 
				longest_start = start; 
				longest_end = end; 

	# If not even a single element follow the property, 
	# then return n 
	if (longest_start == -1): 
		return n; 

	# Return the number of elements to be removed 
	return (n - (longest_end - longest_start + 1)); 

# Driver Code 
arr = [4, 5, 100, 9, 10, 11, 12, 15, 200]; 
n = len(arr); 
print(minRemovalsDP(arr, n)); 