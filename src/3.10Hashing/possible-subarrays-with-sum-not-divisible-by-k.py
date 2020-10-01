# Link: https://www.geeksforgeeks.org/count-of-longest-possible-subarrays-with-sum-not-divisible-by-k/
# https://www.youtube.com/watch?v=ufXxc8Vty9A
# IsDone: 0
# Python3 program for the above problem 

# Function to find the count of 
# longest subarrays with sum not 
# divisible by K 
def CountSubarrays(arr, n, k): 

	# Sum of all elements in 
	# an array 
	s = 0
	for i in range(n): 
		s += arr[i] 

	# If overall sum is not 
	# divisible then return 
	# 1, as only one subarray 
	# of size n is possible 
	if(s % k): 
		return 1
	else: 
		ini = 0

		# Index of the first number 
		# not divisible by K 
		while (ini < n and arr[ini] % k == 0): 
			ini += 1
		final = n - 1

		# Index of the last number 
		# not divisible by K 
		while (final >= 0 and arr[final] % k == 0): 
			final -= 1
			
		sum, count = 0, 0
		
		# Subarray doesn't exist 
		if(ini == n): 
			return -1
		else: 
			length = max(n - 1 - ini, final) 

		# Sum of the window 
		for i in range(length): 
			sum += arr[i] 

		if(sum % k != 0): 
			count += 1

		# Calculate the sum of rest of 
		# the windows of size len 
		for i in range(length, n): # TODO: how it is working
			sum = sum + arr[i] 
			sum = sum - arr[i - length] # i think it should sum - arr to keep it length size window
			if (sum % k != 0): 
				count += 1

		return count 

# Driver Code 
if __name__ == '__main__': 

	arr = [2, 4, 3, 5, 1] 
	n = len(arr) 
	k = 3

	print(CountSubarrays(arr, n, k)) 
	