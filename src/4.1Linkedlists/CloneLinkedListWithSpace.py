#
# A linked list node
class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next

# Helper function to print given linked list
def printList(head):

	ptr = head
	while ptr:
		print(ptr.data)
		ptr = ptr.next

	print("None")

# Function that takes a linked list and returns a complete copy of that
# list using dummy node
def copyList(head):

	current = head  # used to iterate over the original list
	dummy = Node()  # build the list off this dummy node

	# point to the last node in the list
	tail = dummy	# start the tail pointing at the dummy

	while current:
		tail.next = Node(current.data, tail.next)  # add each node at the tail
		tail = tail.next  # advance the tail to the last node
		current = current.next

	return dummy.next

if __name__ == '__main__':

	# construct linked list
	head = None
	for i in reversed(range(4)):
		head = Node(i + 1, head)

	# copy linked list
	dup = copyList(head)

	# print duplicate linked list
	printList(dup)