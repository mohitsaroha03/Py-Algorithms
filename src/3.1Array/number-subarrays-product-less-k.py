# Link: https://www.geeksforgeeks.org/number-subarrays-product-less-k/

# Python3 program to count subarrays 
# having product less than k. 
# https://www.youtube.com/watch?v=NcD0CZLd6xM
# Python3 program to count 
# subarrays having product 
# less than k. 

def countSubArrayProductLessThanK(a,k): 
	n = len(a) 
	p = 1
	res = 0
	start = 0
	end = 0
	while(end < n): 

		# Move right bound by 1 
		# step. Update the product. 
		p *= a[end] 
		
		# Move left bound so guarantee 
		# that p is again less than k. 
		while (start < end and p >= k): 
			p =int(p//a[start]) 
			start+=1
		
		# If p is less than k, update 
		# the counter. Note that this 
		# is working even for (start == end): 
		# it means that the previous 
		# window cannot grow anymore 
		# and a single array element 
		# is the only addendum. 
		if (p < k): 
			l = end - start + 1 # to find the number of subaarays between two indexes
			res += l 
		
		end+=1

	return res 


# Driver Code 
if __name__=='__main__': 
	print(countSubArrayProductLessThanK([1, 2, 3, 4], 10)) 
	print(countSubArrayProductLessThanK([1, 9, 2, 8, 6, 4, 3], 100)) 
	print(countSubArrayProductLessThanK([5, 3, 2], 16)) 
	print(countSubArrayProductLessThanK([100, 200], 100)) 
	print(countSubArrayProductLessThanK([100, 200], 101)) 