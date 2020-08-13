# Link: https://www.techiedelight.com/print-combinations-integers-sum-given-number/
# IsDone: 1
# Recursive function to print all combination of positive integers
# in increasing order that sum to a given number
def printCombinations(A, i, sum, sum_left):

	# To maintain the increasing order, start the loop from
	# previous number stored in A
	prev_num = A[i - 1] if (i > 0) else 1
	for k in range(prev_num, sum + 1):

		# set next element of the list to k
		A[i] = k

		# recur with the sum left and next location in the list
		if sum_left > k:
			printCombinations(A, i + 1, sum, sum_left - k)

		# if sum is found
		if sum_left == k:
			print(A[:i+1])


# Wrapper over printCombinations() function
def findCombinations(sum):

	# create a temporary list for storing the combinations
	A = [0] * sum

	# recur for all combinations
	starting_index = 0
	printCombinations(A, starting_index, sum, sum)


if __name__ == '__main__':

	sum = 5
	findCombinations(sum)