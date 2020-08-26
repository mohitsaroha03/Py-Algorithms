# Link: https://www.geeksforgeeks.org/count-possible-groups-size-2-3-sum-multiple-3/
# Python3 Program to Count groups 
# of size 2 or 3 that have sum 
# as multiple of 3 
# TODO: pending
# Returns count of all possible 
# groups that can be formed 
# from elements of a[]. 
def findgroups(arr, n): 

	# Create an array C[3] to store 
	# counts of elements with 
	# remainder 0, 1 and 2. c[i] 
	# would store count of elements 
	# with remainder i 
	c = [0, 0, 0] 

	# To store the result 
	res = 0

	# Count elements with remainder 
	# 0, 1 and 2 
	for i in range(0, n): 
		c[arr[i] % 3] += 1

	# Case 3.a: Count groups of size 
	# 2 from 0 remainder elements 
	res += ((c[0] * (c[0] - 1)) >> 1) 

	# Case 3.b: Count groups of size 
	# 2 with one element with 1 
	# remainder and other with 2 remainder 
	res += c[1] * c[2] 

	# Case 4.a: Count groups of size 
	# 3 with all 0 remainder elements 
	res += (c[0] * (c[0] - 1) * (c[0] - 2)) / 6

	# Case 4.b: Count groups of size 3 
	# with all 1 remainder elements 
	res += (c[1] * (c[1] - 1) * (c[1] - 2)) / 6

	# Case 4.c: Count groups of size 3 
	# with all 2 remainder elements 
	res += ((c[2] * (c[2] - 1) * (c[2] - 2)) / 6) 

	# Case 4.c: Count groups of size 3 
	# with different remainders 
	res += c[0] * c[1] * c[2] 

	# Return total count stored in res 
	return res 

# Driver program 
arr = [3, 6, 7, 2, 9] 
n = len(arr) 

print ("Required number of groups are", 
			int(findgroups(arr, n))) 