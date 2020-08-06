# Link: https://www.geeksforgeeks.org/count-subarrays-equal-number-1s-0s/
# Python3 implementation to count subarrays 
# with equal number of 1's and 0's 
def countSubarrWithEqualZeroAndOne(arr, n): 
	mp = dict() 
	Sum = 0
	count = 0

	for i in range(n): 

		# Replacing 0's in array with -1 
		if (arr[i] == 0): 
			arr[i] = -1

		Sum += arr[i] 

		# If Sum = 0, it implies number of 
		# 0's and 1's are equal from arr[0]..arr[i] 
		if (Sum == 0): 
			count+=1

		if (Sum in mp.keys()): 
			count += mp[Sum] 

		mp[Sum] = mp.get(Sum, 0) + 1

	return count 

# Driver Code 
arr = [1, 0, 0, 1, 0, 1, 1] 

n = len(arr) 

print("count =", 
	countSubarrWithEqualZeroAndOne(arr, n)) 