# Link: https://www.geeksforgeeks.org/alternate-odd-even-nodes-singly-linked-list/

# Python3 program to rearrange nodes 
# as alternate odd even nodes in 
# a Singly Linked List 

# Structure node 
class Node : 

	def __init__(self): 
		self.data = 0
		self.next = None

# A utility function to print 
# linked list 
def printList(node) : 
	while (node != None) : 
		print(node.data, end = " ") 
		node = node.next
	
	print(" ") 

# Function to create newNode 
# in a linkedlist 
def newNode( key) : 
	temp = Node() 
	temp.data = key 
	temp.next = None
	return temp 

# Function to insert at beginning 
def insertBeg( head, val) : 
	temp = newNode(val) 
	temp.next = head 
	head = temp 
	return head 

# Function to rearrange the 
# odd and even nodes 
def rearrange(head) : 

	# Step 1: Segregate even and odd nodes 
	# Step 2: Split odd and even lists 
	# Step 3: Merge even list into odd list 
	even = None
	temp = None
	prev_temp = None
	i = None
	j = None
	k = None
	l = None
	ptr = None

	# Step 1: Segregate Odd and Even Nodes 
	temp = (head).next
	prev_temp = head 

	while (temp != None) : 
	
		# Backup next pointer of temp 
		x = temp.next

		# If temp is odd move the node 
		# to beginning of list 
		if (temp.data % 2 != 0) : 
		
			prev_temp.next = x 
			temp.next = (head) 
			(head) = temp 
		
		else: 
		
			prev_temp = temp 
		
		# Advance Temp Pointer 
		temp = x 
	
	# Step 2 
	# Split the List into Odd and even 
	temp = (head).next
	prev_temp = (head) 

	while (temp != None and temp.data % 2 != 0) : 
		prev_temp = temp 
		temp = temp.next
	
	even = temp 

	# End the odd List (Make last node None) 
	prev_temp.next = None

	# Step 3: 
	# Merge Even List into odd 
	i = head 
	j = even 

	while (j != None and i != None): 
	
		# While both lists are not 
		# exhausted Backup next 
		# pointers of i and j 
		k = i.next
		l = j.next

		i.next = j 
		j.next = k 

		# ptr points to the latest node added 
		ptr = j 

		# Advance i and j pointers 
		i = k 
		j = l 

	if (i == None): 
	
		# Odd list exhausts before even, 
		# append remainder of even list to odd. 
		ptr.next = j 
		
	# The case where even list exhausts before 
	# odd list is automatically handled since we 
	# merge the even list into the odd list 
	return head 

# Driver Code 
head = newNode(8) 
head = insertBeg(head, 7) 
head = insertBeg(head, 6) 
head = insertBeg(head, 3) 
head = insertBeg(head, 5) 
head = insertBeg(head, 1) 
head = insertBeg(head, 2) 
head = insertBeg(head, 10) 

print("Linked List:" ) 
printList(head) 
print("Rearranged List" ) 
head = rearrange(head) 
printList(head) 
