# Link: hhttps://www.geeksforgeeks.org/number-subarrays-product-less-k/

# Python3 program to count subarrays 
# having product less than k. 

def countsubarray(array, n, k): 
	count = 0
	for i in range(0, n): 
		
		# Counter for single element 
		if array[i] <= k: 
			count += 1

		mul = array[i] 

		for j in range(i + 1, n): 
			
			# Multiple subarray 
			mul = mul * array[j] 
			
			# If this multiple is less 
			# than k, then increment 
			if mul <= k: 
				count += 1
			else: 
				break
	return count 

# Driver Code 
array = [ 1, 2, 3, 4 ] 
k = 10
size = len(array) 
count = countsubarray(array, size, k); 
print (count, end = " ") 
