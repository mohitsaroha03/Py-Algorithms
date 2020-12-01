# Link: https://www.geeksforgeeks.org/count-possible-ways-to-construct-buildings/
# Python 3 program to count all possible 
# way to construct buildings 


# Returns count of possible ways 
# for N sections 
def countWays(N) : 

	# Base case 
	if (N == 1) : 
		# 2 for one side and 4 
		# for two sides 
		return 4

	# countB is count of ways with a 
	# building at the end 
	# countS is count of ways with a 
	# space at the end 
	# prev_countB and prev_countS are 
	# previous values of 
	# countB and countS respectively. 

	# Initialize countB and countS 
	# for one side 
	countB=1
	countS=1

	# Use the above recursive formula 
	# for calculating 
	# countB and countS using previous values 
	for i in range(2,N+1) : 
	
		prev_countB = countB 
		prev_countS = countS 

		countS = prev_countB + prev_countS 
		countB = prev_countS 
	

	# Result for one side is sum of ways 
	# ending with building 
	# and ending with space 
	result = countS + countB 

	# Result for 2 sides is square of 
	# result for one side 
	return (result*result) 


# Driver program 
if __name__ == "__main__": 

	N = 3
	print ("Count of ways for ", N 
		," sections is " ,countWays(N)) 