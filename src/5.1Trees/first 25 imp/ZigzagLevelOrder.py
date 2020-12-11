# Link: https://www.geeksforgeeks.org/zigzag-tree-traversal/
# IsDone: 1

# Python Program to print zigzag traversal 
# of binary tree 

# Binary tree node 
class Node: 
	# Constructor to create a new node 
	def __init__(self, data): 
		self.data = data 
		self.left = self.right = None


# function to print zigzag traversal of 
# binary tree  

def zizagtraversal(root): # Iterative solution

	# Base Case 
	if root is None: 
		return

	# Create two stacks to store current 
	# and next level 
	currentLevel = [] 
	nextLevel = [] 

	# if ltr is true push nodes from 
	# left to right otherwise from 
	# right to left 
	ltr = True

	# append root to currentlevel stack 
	currentLevel.append(root) 

	# Check if stack is empty 
	while len(currentLevel) > 0: 
		# pop from stack 
		temp = currentLevel.pop(-1) 
		# print the data 
		print(temp.data, " ") 

		if ltr: 
			# if ltr is true push left 
			# before right 
			if temp.left: 
				nextLevel.append(temp.left) 
			if temp.right: 
				nextLevel.append(temp.right) 
		else: 
			# else push right before left 
			if temp.right: 
				nextLevel.append(temp.right) 
			if temp.left: 
				nextLevel.append(temp.left) 

		if len(currentLevel) == 0: 
			# reverse ltr to push node in 
			# opposite order 
			ltr = not ltr 
			# swapping of stacks 
			currentLevel, nextLevel = nextLevel, currentLevel 

# Recursive Function to find height 
# of binary tree 
def heightOfTree(root): 

	if root == None: 
		return 0
	
	lheight = heightOfTree(root.left) 
	rheight = heightOfTree(root.right) 
	
	return max(lheight + 1, rheight + 1) 

def heightOfTree2(root, H): # another variationof height of tree root, 0

	if root == None: 
		return H
	
	lheight = heightOfTree(root.left, H+1) 
	rheight = heightOfTree(root.right, H+1) 
	
	return max(lheight , rheight) 

# Function to print nodes from right to left 
def printRightToLeft(root, level): 

	if root == None: 
		return
	
	if level == 1: 
		print(root.data) 
	
	elif level > 1: 
	
		printRightToLeft(root.right, level - 1) 
		printRightToLeft(root.left, level - 1) 

# Function to print nodes from left to right 
def printLeftToRight(root, level): 

	if root == None: 
		return
	
	if level == 1: 
		print(root.data) 
	
	elif level > 1: 
	
		printLeftToRight(root.left, level - 1) 
		printLeftToRight(root.right, level - 1) 

# Function to print Reverse ZigZag of 
# a Binary tree 
def printZigZag(root): # recursive solution

	# Flag is used to mark the 
	# change in level 
	flag = 0
	
	# Height of tree 
	height = heightOfTree(root) 
	
	for i in range(1, height + 1): 
	
		# If flag value is one print nodes 
		# from right to left 
		if flag == 1: 
		
			printRightToLeft(root, i) 
			
			# Mark flag as zero so that next time 
			# nodes are printed from left to right 
			flag = 0
		
		# If flag is zero print nodes 
		# from left to right 
		elif flag == 0: 
		
			printLeftToRight(root, i) 
			
			# Mark flag as one so that next time 
			# nodes are printed from right to left 
			flag = 1
		
# Driver code 
if __name__ == "__main__": 

	root = Node(7) 
	root.left = Node(4) 
	root.right = Node(5) 
	root.left.left = Node(9) 
	root.right.right = Node(10) 
	root.left.left.left = Node(6) 
	root.left.left.right = Node(11) 
	
	# root = Node(1) 
	# root.left = Node(2) 
	# root.right = Node(3) 
	# root.left.left = Node(7) 
	# root.left.right = Node(6) 
	# root.right.left = Node(5) 
	# root.right.right = Node(4) 
	print("Zigzag Order traversal iterative") 
	zizagtraversal(root) 
	print("Zigzag traversal recursive") 
	printZigZag(root) # recursive
