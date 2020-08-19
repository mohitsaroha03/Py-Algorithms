# Link: https://www.geeksforgeeks.org/squarerootnth-node-in-a-linked-list/

# Python3 program to find sqrt(n)'th node 
# of a linked list 

# Node class 
class Node: 

	# Function to initialise the node object 
	def __init__(self, data): 
		self.data = data 
		self.next = None

# Function to get the sqrt(n)th 
# node of a linked list 
def printsqrtn(head) : 

	sqrtn = None
	i = 1
	j = 1
	
	# Traverse the list 
	while (head != None) : 
	
		# check if j = sqrt(i) 
		if (i == j * j) : 
		
			# for first node 
			if (sqrtn == None) : 
				sqrtn = head 
			else: 
				sqrtn = sqrtn.next
			
			# increment j if j = sqrt(i) 
			j = j + 1
		
		i = i + 1
		
		head = head.next
	
	# return node's data 
	return sqrtn.data 

def print_1(head) : 

	while (head != None) : 
		print( head.data,) 
		head = head.next
	print(" ") 

# function to add a new node at the 
# beginning of the list 
def push(head_ref, new_data) : 

	# allocate node 
	new_node = Node(0) 
	
	# put in the data 
	new_node.data = new_data 
	
	# link the old list off the new node 
	new_node.next = (head_ref) 
	
	# move the head to point to the new node 
	(head_ref) = new_node 
	return head_ref 

# Driver Code 
if __name__=='__main__': 

	# Start with the empty list 
	head = None
	head = push(head, 40) 
	head = push(head, 30) 
	head = push(head, 20) 
	head = push(head, 10) 
	print("Given linked list is:") 
	print_1(head) 
	print("sqrt(n)th node is ", 
			printsqrtn(head)) 