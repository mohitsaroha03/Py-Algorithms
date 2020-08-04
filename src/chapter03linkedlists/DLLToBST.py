# Link: https://www.techiedelight.com/construct-height-balanced-bst-from-sorted-doubly-linked-list/
# Data structure to store node of Doubly Linked List / BST
class Node:
	# The prev and next pointer of the Doubly Linked List can act as
	# left and right child pointer for the BST respectively
	def __init__(self, data, prev=None, next=None):
		self.data = data
		self.prev = prev
		self.next = next


# Function to insert a node at the beginning of the Doubly Linked List
def push(head, data):

	# allocate a node and link it at the beginning
	node = Node(data)
	node.next = head

	# change prev of the existing head node to point to the node
	if head:
		head.prev = node

	# update head pointer
	head = node
	return head


# Function to print and count number of nodes in a Doubly Linked List
def printAndCountNodes(node):

	counter = 0

	while node:
		print(node.data)
		node = node.next
		counter = counter + 1

	print()
	return counter


# Function to print pre-order traversal of the BST
def preorder(root):

	if root is None:
		return

	print(root.data)
	preorder(root.prev)
	preorder(root.next)


# Recursive function to construct a height-balanced BST from a sorted Doubly
# Linked List. It takes the head node of the Doubly Linked List and
# number of nodes in the Doubly Linked List as argument
def convertSortedDLLToBalancedBST(head, n):

	# base case
	if n <= 0:
		return None, head

	# recursively construct the left subtree
	leftSubTree, head = convertSortedDLLToBalancedBST(head, n // 2)

	# head now points to the middle node of the sorted DDL

	# make mid node of the sorted DDL as root node of the BST
	root = head

	# update left child of the root node
	root.prev = leftSubTree

	# update the head reference of the DLL
	head = head.next

	# recursively construct the right subtree with the remaining nodes
	root.next, head = convertSortedDLLToBalancedBST(head, n - (n // 2 + 1))
														# +1 for the root

	# return the root node
	return root, head


if __name__ == '__main__':

	# Points to the head of a Doubly Linked List
	head = None

	# Construct a Doubly Linked List from sorted keys
	keys = [25, 20, 18, 15, 12, 10, 8]
	for key in keys:
		head = push(head, key)

	# print the list and count number of nodes
	print("Doubly Linked List: ")
	n = printAndCountNodes(head)

	# Construct a height-balanced BST from a sorted Doubly Linked List
	root, head = convertSortedDLLToBalancedBST(head, n)

	print("Preorder traversal of the constructed BST: ")
	preorder(root)
