# isGFG: , Link: 
# IsDone: 0
import sys
class BSTNode:
    def __init__(root, data):
        root.left = None
        root.right = None
        root.data = data

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

prev = None
def FloorInBST(root, data):
	global prev
	return FloorInBSTUtil(root, data)

def FloorInBSTUtil(root, data):
	if(not root): 
		return sys.maxint

	if(root.data == data) :
		return root.data

	if(data < root.data): 	
		return FloorInBSTUtil(root.left, data)

	floor = FloorInBSTUtil(root.right, data)
	if floor <= data:
		return floor
	else: return root.data 
		
root = BSTNode(3)
insertNode(root, BSTNode(17))
insertNode(root, BSTNode(11))
insertNode(root, BSTNode(55))
insertNode(root, BSTNode(23))
insertNode(root, BSTNode(99))
# inOrderTraversal(root)
for i  in range(100):
	print i, "floor is ", FloorInBSTUtil(root, i)
