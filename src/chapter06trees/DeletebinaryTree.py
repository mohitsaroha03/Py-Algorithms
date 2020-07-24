# isGFG: , Link: 
# IsDone: 1
# Python3 program to count all nodes 
# having k leaves in subtree rooted with them 

# A binary tree node has data, pointer to 
# left child and a pointer to right child 
# Helper function that allocates a new node 
# with the given data and None left and 
# right pointers 
class newNode: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

''' This function is same as deleteTree() 
in the previous program '''
def _deleteTree(node): 
	if (node == None): 
		return

	# first delete both subtrees 
	_deleteTree(node.left) 
	_deleteTree(node.right) 

	# then delete the node 
	print("Deleting node: ", 
				node.data) 
	node = None
	
# Deletes a tree and sets the root as NULL 
def deleteTree(node_ref): 
	_deleteTree(node_ref) 
	node_ref = None

# Inorder traversal of a binary tree 
def inorder(temp): 
    if(not temp): 
        return
    inorder(temp.left) 
    print temp.data
    inorder(temp.right) 
   
# function to delete the given deepest node (d_node) in binary tree  
def deleteDeepest(root,d_node): 
    q = [] 
    q.append(root) 
    while(len(q)): 
        temp = q.pop(0) 
        if temp is d_node: 
            temp = None
            return
        if temp.right: 
            if temp.right is d_node: 
                temp.right = None
                return
            else: 
                q.append(temp.right) 
        if temp.left: 
            if temp.left is d_node: 
                temp.left = None
                return
            else: 
                q.append(temp.left) 
   
# function to delete element in binary tree  
def deletion(root, key): 
    if root == None : 
        return None
    if root.left == None and root.right == None: 
        if root.key == key :  
            return None
        else : 
            return root 
    key_node = None
    q = [] 
    q.append(root) 
    while(len(q)): 
        temp = q.pop(0) 
        if temp.data == key: 
            key_node = temp 
        if temp.left: 
            q.append(temp.left) 
        if temp.right: 
            q.append(temp.right) 
    if key_node :  
        x = temp.data 
        deleteDeepest(root,temp) 
        key_node.data = x 
    return root 
   
# Driver code 
root = newNode(10) 
root.left = newNode(11) 
root.left.left = newNode(7) 
root.left.right = newNode(12) 
root.right = newNode(9) 
root.right.left = newNode(15) 
root.right.right = newNode(8) 
print("The tree before the deletion:") 
inorder(root) 
key = 11
root = deletion(root, key) 
print() 
print("The tree after the deletion;") 
inorder(root) 

# Driver code 
# root = [0] 

root1 = newNode(1) 
root1.left = newNode(2) 
root1.right = newNode(3) 
root1.left.left = newNode(4) 
root1.left.right = newNode(5) 

# Note that we pass the address 
# of root1 here 
print("Tree deleted : ") 
deleteTree(root1)