# Link: https://www.geeksforgeeks.org/find-whether-subarray-form-mountain-not/
# Python 3 program to check whether a subarray is in 
# mountain form or not 

# Utility method to construct left and right array 
def preprocess(arr, N, left, right): 
	# initialize first left index as that index only 
	left[0] = 0
	lastIncr = 0

	for i in range(1,N): 
		# if current value is greater than previous, 
		# update last increasing 
		if (arr[i] > arr[i - 1]): 
			lastIncr = i 
		left[i] = lastIncr 

	# initialize last right index as that index only 
	right[N - 1] = N - 1
	firstDecr = N - 1

	i = N - 2
	while(i >= 0): 
		# if current value is greater than next, 
		# update first decreasing 
		if (arr[i] > arr[i + 1]): 
			firstDecr = i 
		right[i] = firstDecr 
		i -= 1

# method returns true if arr[L..R] is in mountain form 
def isSubarrayMountainForm(arr, left, right, L, R): 
	
	# return true only if right at starting range is 
	# greater than left at ending range 
	return (right[L] >= left[R]) 

# Driver code 
if __name__ == '__main__': 
	arr = [2, 3, 2, 4, 4, 6, 3, 2] 
	N = len(arr) 

	left = [0 for i in range(N)] 
	right = [0 for i in range(N)] 
	preprocess(arr, N, left, right) 

	L = 0
	R = 2
	if (isSubarrayMountainForm(arr, left, right, L, R)): 
		print("Subarray is in mountain form") 
	else: 
		print("Subarray is not in mountain form") 

	L = 1
	R = 3
	if (isSubarrayMountainForm(arr, left, right, L, R)): 
		print("Subarray is in mountain form") 
	else: 
		print("Subarray is not in mountain form") 
