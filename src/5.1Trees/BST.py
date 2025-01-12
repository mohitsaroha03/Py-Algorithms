# Link: https://www.geeksforgeeks.org/binary-search-tree-data-structure/
# IsDone: 1

# A Binary Tree Node 
class Node:

    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# A utility function to do inorder traversal of BST 
def inorder(root):
    if root is not None:
        inorder(root.left)
        print root.key,
        inorder(root.right)


def reverseinorder(root):
    if root is not None:
        inorder(root.right)
        print root.key,
        inorder(root.left)

# A utility function to insert a new node with given key in BST

def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    # return the (unchanged) node pointer
    return node


# Given a non-empty binary search tree, return the node 
# with minum key value found in that tree. Note that the 
# entire tree does not need to be searched 
def minValueNode(node):
    current = node

    # loop down to find the leftmost leaf
    while (current.left is not None):
        current = current.left

    return current


# Given a binary search tree and a key, this function 
# delete the key and returns the new root 
# link: https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/

def deleteNode(root, key):
    # Base Case
    if root is None:
        return root

    # If the key to be deleted is smaller than the root's
    # key then it lies in left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)

    # If the kye to be delete is greater than the root's key
    # then it lies in right subtree
    elif (key > root.key):
        root.right = deleteNode(root.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's content to this node
        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)

    return root


# link: https://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
def LowestCommonAncestor(root, n1, n2):
    if root is None:
        return None

    # If both n1 and n2 are smaller than root, then LowestCommonAncestor 
    # lies in left 
    if (root.key > n1 and root.key > n2):
        return LowestCommonAncestor(root.left, n1, n2)

        # If both n1 and n2 are greater than root, then LowestCommonAncestor
    # lies in right  
    if (root.key < n1 and root.key < n2):
        return LowestCommonAncestor(root.right, n1, n2)

    return root


# Driver program to test above functions 
""" Let us create following BST 
		  50 
		/	 \ 
	  48	 61 
	  / \   / \ 
	20  49 60 80 """

root = None
root = insert(root, 50)
root = insert(root, 48)
root = insert(root, 20)
root = insert(root, 49)
root = insert(root, 61)
root = insert(root, 60)
root = insert(root, 80)

print "Inorder traversal of the given tree"
inorder(root)

print "Inorder traversal of the modified tree"
inorder(root)

print "Inorder traversal of the modified tree"
inorder(root)

print "Inorder traversal of the modified tree"
inorder(root)

print "\n Find LowestCommonAncestor: "
print LowestCommonAncestor(root, 60, 20).key

print "\nDelete 20: "
root = deleteNode(root, 30)
inorder(root)
print "\nDelete 30: "
root = deleteNode(root, 30)
inorder(root)
print "\nDelete 50: "
root = deleteNode(root, 50)
inorder(root)