# Link: https://www.geeksforgeeks.org/minimum-number-platforms-required-railwaybus-station/
# Program to find minimum 
# number of platforms 
# required on a railway 
# station 
# TODO: https://practice.geeksforgeeks.org/problems/maximum-tip-calculator/0
# TODO: https://practice.geeksforgeeks.org/problems/rubiks-cube/0
# Returns minimum number 
# of platforms reqquired 
def findPlatform(arr, dep, n): 

	# Sort arrival and 
	# departure arrays 
	arr.sort() 
	dep.sort() 

	# plat_needed indicates 
	# number of platforms 
	# needed at a time 
	plat_needed = 1
	result = 1
	i = 1
	j = 0

	# Similar to merge in 
	# merge sort to process 
	# all events in sorted order 
	while (i < n and j < n): 
	
		# If next event in sorted 
		# order is arrival, 
		# increment count of 
		# platforms needed 
		if (arr[i] <= dep[j]): 
		
			plat_needed+= 1
			i+= 1
		

		# Else decrement count 
		# of platforms needed 
		elif (arr[i] > dep[j]): 
		
			plat_needed-= 1
			j+= 1

		# Update result if needed 
		if (plat_needed > result): 
			result = plat_needed 
		
	return result 

# driver code 

arr = [900, 940, 950, 1100, 1500, 1800] 
dep = [910, 1200, 1120, 1130, 1900, 2000] 
n = len(arr) 

print("Minimum Number of Platforms Required = ", 
		findPlatform(arr, dep, n)) 