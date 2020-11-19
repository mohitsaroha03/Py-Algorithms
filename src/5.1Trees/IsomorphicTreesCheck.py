# Link: 
# IsDone: 0
'''Binary Tree Class and its methods'''
class BinaryTree:
	def __init__(self, data):
		self.data = data  # root node
		self.left = None  # left child
		self.right = None  # right child
	# set data
	def set_data(self, data):
		self.data = data
	# get data   
	def get_data(self):
		return self.data	
	# get left child of a node
	def getLeft(self):
		return self.left
	# get right child of a node
	def getRight(self):
		return self.right
	# get left child of a node
	def setLeft(self, left):
		self.left = left
	# get right child of a node
	def setRight(self, right):
		self.right = right
	def insertLeft(self, newNode):
		if self.left == None:
			self.left = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.left = self.left
			self.left = temp

	def insertRight(self, newNode):
		if self.right == None:
			self.right = BinaryTree(newNode)
		else:
			temp = BinaryTree(newNode)
			temp.right = self.right
			self.right = temp
	  
def isIsomorphic(root1, root2):
	if(not root1 and not root2): 
		return 1
	if((not root1 and root2) or (root1 and not root2)):
	    return 0
	return (isIsomorphic(root1.left, root2.left) and isIsomorphic(root1.right, root2.right))
		

root1 = BinaryTree(11)
root1.insertLeft(1)
root1.insertLeft(10)
root1.insertLeft(1100)
root1.insertRight(5)
root1.getRight().set_data(2)

root2 = BinaryTree(99)
root2.insertLeft(9)
root2.insertLeft(910)
root2.insertLeft(9900)
root2.insertRight(8)
root2.getRight().set_data(2)
print "Isomorphic:", isIsomorphic(root1, root2)
