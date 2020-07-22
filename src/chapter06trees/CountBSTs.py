''

def CountTrees(n) :
	if (n <= 1):   
		return 1
	else :	
		# there will be one value at the root, with whatever remains on the left and right
		# each forming their own subtrees. Iterate through all the values that could be the root...
		sum = 0
		for root in range(1, n + 1):
			left = CountTrees(root - 1)
			right = CountTrees(n - root)
			# number of possible trees with this root == left*right
			sum += left * right

		return(sum)
for i  in range(1, 11):
	print CountTrees(i)
