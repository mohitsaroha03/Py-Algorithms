# isGFG: , Link: 
# IsDone: 0
# Returns 1 if A[] can be partitioned in two subsets of equal sum, otherwise 0
def findPartition(A):
	# calculate sum of all elements
	sum = 0
	n = len(A)
	for i in range(0, n):
		sum += A[i]
	# If sum is odd, there cannot be two subsets with equal sum
	if (sum % 2 != 0):
		return 0

	Table = [[0 for x in range(n + 1)] for x in range(sum // 2 + 1)]

	# initialize top row as true
	for i in range(0, n):
		Table[0][i] = 1

	# initialize leftmost column, except Table[0][0], as 0
	for i in range(1, sum // 2 + 1):
		Table[i][0] = 0

	# Fill the partition table in bottom up manner
	for i in range(1, sum // 2 + 1):
		for j in range(0, n + 1):
			Table[i][j] = Table[i][j - 1]
			if (i >= A[j - 1]):
				Table[i][j] = Table[i][j] or Table[i - A[j - 1]][j - 1]
	return Table[sum / 2][n]
