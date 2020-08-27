# Link: https://www.geeksforgeeks.org/longest-subarray-sum-divisible-k/
# Python 3 implementation to find the 
# longest subarray with sum divisible by k 
# TODO: pending
# function to find the longest 
# subarray with sum divisible by k 
def longSubarrWthSumDivByK(arr, n, k): 
	
	# unodered map 'um' implemented 
	# as hash table 
	um = {i:0 for i in range(8)} 

	# 'mod_arr[i]' stores (sum[0..i] % k) 
	mod_arr = [0 for i in range(n)] 
	max = 0
	curr_sum = 0
	
	# traverse arr[] and build up 
	# the array 'mod_arr[]' 
	for i in range(n): 
		curr_sum += arr[i] 
		
		# as the sum can be negative, 
		# taking modulo twice 
		mod_arr[i] = ((curr_sum % k) + k) % k 
	
	for i in range(n): 
		
		# if true then sum(0..i) is 
		# divisible by k 
		if (mod_arr[i] == 0): 
			
			# update 'max' 
			max = i + 1
		
		# if value 'mod_arr[i]' not present in 
		# 'um' then store it in 'um' with index 
		# of its first occurrence 
		elif (mod_arr[i] in um): 
			um[mod_arr[i]] = i 
			
		else: 
			
			# if true, then update 'max' 
			if (max < (i - um[mod_arr[i]])): 
				max = i - um[mod_arr[i]]		 
	
	# required length of longest subarray 
	# with sum divisible by 'k' 
	return max		

# Driver Code 
if __name__ == '__main__': 
	arr = [2, 7, 6, 1, 4, 5] 
	n = len(arr) 
	k = 3
	
	print("Length =", 
		longSubarrWthSumDivByK(arr, n, k)) 