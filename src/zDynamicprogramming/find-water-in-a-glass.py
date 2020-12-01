# Link: https://www.geeksforgeeks.org/find-water-in-a-glass/
# Program to find the amount 
# of water in j-th glass of
# i-th row

# Returns the amount of water 
# in jth glass of ith row
def findWater(i, j, X):
	# A row number i has maximum
	# i columns. So input column 
	# number must be less than i
	if (j > i):
		print("Incorrect Input");
		return;

	# There will be i*(i+1)/2 
	# glasses till ith row 
	# (including ith row)
	# and Initialize all glasses 
	# as empty
	glass = [0]*int(i *(i + 1) / 2);

	# Put all water
	# in first glass
	index = 0;
	glass[index] = X;

	# Now let the water flow to 
	# the downward glasses till
	# the row number is less 
	# than or/ equal to i (given 
	# row) correction : X can be 
	# zero for side glasses as 
	# they have lower rate to fill
	for row in range(1,i):
		# Fill glasses in a given
		# row. Number of columns 
		# in a row is equal to row number
		for col in range(1,row+1):
			# Get the water 
			# from current glass
			X = glass[index];

			# Keep the amount less 
			# than or equal to
			# capacity in current glass
			glass[index] = 1.0 if (X >= 1.0) else X;

			# Get the remaining amount
			X = (X - 1) if (X >= 1.0) else 0.0;

			# Distribute the remaining 
			# amount to the down two glasses
			glass[index + row] += (X / 2);
			glass[index + row + 1] += (X / 2);
			index+=1;

	# The index of jth glass
	# in ith row will 
	# be i*(i-1)/2 + j - 1
	return glass[int(i * (i - 1) /2 + j - 1)];

# Driver Code
if __name__ == "__main__":
	
	i = 2;
	j = 2;
	X = 2.0; 
# Total amount of water

	res=repr(findWater(i, j, X));
	print("Amount of water in jth glass of ith row is:",res.ljust(8,'0'));