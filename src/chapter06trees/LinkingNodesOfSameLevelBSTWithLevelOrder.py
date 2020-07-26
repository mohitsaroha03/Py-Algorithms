# Link: 
# IsDone: 1
# Node of a Singly Linked List
class Node:
	# constructor
	def __init__(self, data=None, next=None):
		self.data = data
		self.last = None
		self.next = next
	# method for setting the data field of the node    
	def set_data(self, data):
		self.data = data
	# method for getting the data field of the node   
	def get_data(self):
		return self.data
	# method for setting the next field of the node
	def set_next(self, next):
		self.next = next
	# method for getting the next field of the node    
	def get_next(self):
		return self.next
	# method for setting the last field of the node
	def setLast(self, last):
		self.last = last
	# method for getting the last field of the node    
	def getLast(self):
		return self.last	
	# returns true if the node points to another node
	def has_next(self):
		return self.next != None

class Queue(object):
	def __init__(self, data=None):
		self.front = None
		self.rear = None
		self.size = 0

	def enQueue(self, data):
		self.lastNode = self.front
		self.front = Node(data, self.front)
		if self.lastNode:
			self.lastNode.setLast(self.front)
		if self.rear is None:
			self.rear = self.front
		self.size += 1

	def queueRear(self):
		if self.rear is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		return self.rear.get_data()

	def queueFront(self):
		if self.front is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		return self.front.get_data()

	def deQueue(self):
		if self.rear is None:
			print "Sorry, the queue is empty!"
			raise IndexError
		result = self.rear.get_data()
		self.rear = self.rear.last
		self.size -= 1
		return result

	def size(self):
		return self.size
		
	def isEmpty(self):
		return self.size == 0

import sys
class BSTNode:
    def __init__(root, data):
        root.left = None
        root.right = None
        root.data = data
	root.next = None

def insertNode(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.left == None:
                root.left = node
            else:
                insertNode(root.left, node)
        else:
            if root.right == None:
                root.right = node
            else:
                insertNode(root.right, node)

def deleteNode(root, data):
	""" delete the node with the given data and return the root node of the tree """	    
	if root.data == data:
		# found the node we need to delete
		if root.right and root.left: 
			# get the successor node and its parent 
			[psucc, succ] = findMin(root.right, root)
			# splice out the successor
			# (we need the parent to do this) 
			if psucc.left == succ:
				psucc.left = succ.right
			else:
				psucc.right = succ.right					
			# reset the left and right children of the successor
			succ.left = root.left
			succ.right = root.right
			return succ                
		else:
			# "easier" case
			if root.left:
				return root.left  # promote the left subtree
			else:
				return root.right  # promote the right subtree 
	else:
		if root.data > data:  # data should be in the left subtree
			if root.left:
				root.left = deleteNode(root.left, data)
			# else the data is not in the tree 
		else:  # data should be in the right subtree
			if root.right:
				root.right = deleteNode(root.right, data)
	return root

def findMin(root, parent):
	""" return the minimum node in the current tree and its parent """
	# we use an ugly trick: the parent node is passed in as an argument
	# so that eventually when the leftmost child is reached, the 
	# call can return both the parent to the successor and the successor
	if root.left:
		return findMin(root.left, root)
	else:
		return [parent, root]

def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.left)
    print root.data
    inOrderTraversal(root.right)

def preOrderTraversal(root):
    if not root:
        return        
    print root.data
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)    


def PruneBST(root, A, B):
	if(not root):  
		return None
	root.left = PruneBST(root.left, A, B)
	root.right = PruneBST(root.right, A, B)
	if(A <= root.data and root.data <= B):
		return root
	if(root.data < A):
		return root.right
	if(root.data > B):
		return root.left


def linkingNodesOfSameLevel(root):
	Q = Queue()
	if(not root):
		return
	Q.enQueue(root)
	currentLevelNodeCount = 1
	nextLevelNodeCount = 0
	prev = None
	while (not Q.isEmpty()) :
		temp = Q.deQueue()
		if (temp.left):
			Q.enQueue(temp.left)
			nextLevelNodeCount += 1

		if (temp.right):
			Q.enQueue(temp.right)
			nextLevelNodeCount += 1

		# Link the previous node of the current level to this node
		if (prev):
			prev.next = temp
		# Set the previous node to the current 
		prev = temp
		currentLevelNodeCount -= 1
		if (currentLevelNodeCount == 0) :  # if this is the last node of the current level
			currentLevelNodeCount = nextLevelNodeCount
			nextLevelNodeCount = 0
			prev = None    

root = BSTNode(3)
insertNode(root, BSTNode(17))
insertNode(root, BSTNode(11))
insertNode(root, BSTNode(55))
insertNode(root, BSTNode(23))
insertNode(root, BSTNode(99))
root = PruneBST(root, 10, 99)
inOrderTraversal(root)
linkingNodesOfSameLevel(root)
