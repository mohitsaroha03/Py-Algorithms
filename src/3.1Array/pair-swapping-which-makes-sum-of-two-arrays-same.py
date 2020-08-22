# Link: https://www.geeksforgeeks.org/find-a-pair-swapping-which-makes-sum-of-two-arrays-same/
# Python code for optimized implementation 

#Returns sum of elements in list 
def getSum(X): 
	sum=0
	for i in X: 
		sum+=i 
	return sum

# Finds value of 
# a - b = (sumA - sumB) / 2 
def getTarget(A,B): 
	# Calculations of sumd from both lists 
	sum1=getSum(A) 
	sum2=getSum(B) 

	# Because that target must be an integer 
	if( (sum1-sum2)%2!=0): 
		return 0
	return (sum1-sum2)/2

# Prints elements to be swapped 
def findSwapValues(A,B): 
	# Call for sorting the lists 
	A.sort() 
	B.sort() 

	#Note that target can be negative 
	target=getTarget(A,B) 

	# target 0 means, answer is not possible 
	if(target==0): 
		return
	i,j=0,0
	while(i<len(A) and j<len(B)): 
		diff=A[i]-B[j] 
		if diff == target: 
			print A[i],B[j] 
			return
		# Look for a greater value in list A 
		elif diff <target: 
			i+=1
		# Look for a greater value in list B 
		else: 
			j+=1

A=[4,1,2,1,1,2] 
B=[3,6,3,3] 

findSwapValues(A,B) 