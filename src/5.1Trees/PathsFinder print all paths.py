# Link: https://www.geeksforgeeks.org/given-a-binary-tree-print-all-root-to-leaf-paths/
# IsDone: 0
# Python3 program to print all of its 
# root-to-leaf paths for a tree 
class Node: 
	
	# A binary tree node has data, 
	# pointer to left child and a 
	# pointer to right child 
	def __init__(self, data): 
		self.data = data 
		self.right = None
		self.left = None

def printRoute(stack, root): 
	if root == None: 
		return
		
	# append this node to the path array 
	stack.append(root.data) 
	if(root.left == None and root.right == None): 
		
		# print out all of its 
		# root - to - leaf 
		print(' '.join([str(i) for i in stack])) 
		
	# otherwise try both subtrees 
	printRoute(stack, root.left) 
	printRoute(stack, root.right) 
	stack.pop() 

# Driver Code 
root = Node(1); 
root.left = Node(2); 
root.right = Node(3); 
root.left.left = Node(4); 
root.left.right = Node(5); 
printRoute([], root) 