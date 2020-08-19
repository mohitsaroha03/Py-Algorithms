
# A linked list node
class Node:
	def __init__(self, data, left=None, right=None, next=None):
		self.data = data
		self.left = left
		self.right = right
		self.next = next


# Utility function to print contents of a linked list
def printList(node):

	while node:
		print(node.data)
		node = node.next
	print("None")


# Takes two lists sorted in increasing order, and merge their nodes
# together to make one big sorted list which is returned
def sortedMerge(a, b):

	# Base cases
	if a is None:
		return b
	elif b is None:
		return a

	# Pick either a or b, and recur
	if a.data <= b.data:
		result = a
		result.next = sortedMerge(a.next, b)
	else:
		result = b
		result.next = sortedMerge(a, b.next)

	return result


# The main function to merge given k sorted linked lists
# It takes a list of lists A[0..k) and generates the sorted output
def mergeKLists(A, k):

	last = k - 1

	# repeat until only one list is left
	while last:
		(i, j) = (0, last)

		# (i, j) forms a pair
		while i < j:
			# merge List i with List j and store
			# merged list in List i
			A[i] = sortedMerge(A[i], A[j])

			# consider next pair
			i = i + 1
			j = j - 1

			# If all pairs are merged, update last
			if i >= j:
				last = j

	return A[0]


if __name__ == '__main__':

	k = 3	   # Number of linked lists

	# A list to store the head nodes of the linked lists
	A = [Node] * k

	A[0] = Node(1)
	A[0].next = Node(5)
	A[0].next.next = Node(7)

	A[1] = Node(2)
	A[1].next = Node(3)
	A[1].next.next = Node(6)
	A[1].next.next.next = Node(9)

	A[2] = Node(4)
	A[2].next = Node(8)
	A[2].next.next = Node(10)

	# Merge all lists into one
	head = mergeKLists(A, k)
	printList(head)
