# Link: 
# IsDone: 1
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

count = 0
def kthSmallestInBST(root, k):
	global count
	if(not root): 
		return None
	left = kthSmallestInBST(root.left, k)
	if(left): 
		return left
	count += 1
	if(count == k): 
		return root
	return kthSmallestInBST(root.right, k)

	#    2
	# 1    7
	#    5   9
root = BSTNode(3)
insertNode(root, BSTNode(2))
insertNode(root, BSTNode(1))
insertNode(root, BSTNode(7))
insertNode(root, BSTNode(5))
# insertNode(root, BSTNode(2))
insertNode(root, BSTNode(9))
# inOrderTraversal(root)
print kthSmallestInBST(root, 3).data
