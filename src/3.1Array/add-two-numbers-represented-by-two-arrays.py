# Link: https://www.geeksforgeeks.org/add-two-numbers-represented-by-two-arrays/
# Python3 code to sum two numbers 
# representer two arrays. 

# Return sum of two number represented 
# by the arrays. Size of a[] is greater 
# than b[]. It is made sure be the 
# wrapper function 
def calSumUtil( a , b , n , m ): 
	# array to store sum. 
	sum = [0] * n 
	i = n - 1
	j = m - 1
	k = n - 1
	
	carry = 0
	s = 0
	
	# Until we reach beginning of array. 
	# we are comparing only for second array 
	# because we have already compare the size 
	# of array in wrapper function. 
	while j >= 0: 

		# find sum of corresponding element 
		# of both array. 
		s = a[i] + b[j] + carry 
		sum[k] = (s % 10) 
		
		# Finding carry for next sum. 
		carry = s // 10
		
		k-=1
		i-=1
		j-=1
	
	# If second array size is less the first 
	# array size. 
	while i >= 0: 

		# Add carry to first array elements. 
		s = a[i] + carry 
		sum[k] = (s % 10) 
		carry = s // 10
		
		i-=1
		k-=1
	
	ans = 0
	# If there is carry on adding 0 index elements. 
	# append 1 to total sum. 
	if carry: 
		ans = 10
	
	# Converting array into number. 
	for i in range(n): 
		ans += sum[i] 
		ans *= 10
	
	return ans // 10

# Wrapper Function 
def calSum(a, b, n, m ): 

	# Making first array which have 
	# greater number of element 
	if n >= m: 
		return calSumUtil(a, b, n, m) 
	else: 
		return calSumUtil(b, a, m, n) 

# Driven Code 
a = [ 9, 3, 9 ] 
b = [ 6, 1 ] 
n = len(a) 
m = len(b) 
print(calSum(a, b, n, m)) 