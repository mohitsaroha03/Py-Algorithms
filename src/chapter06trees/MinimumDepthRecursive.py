# isGFG: , Link: 
# IsDone: 0
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:  
    def minimumDepth(self, root): 
        # If root (tree) is empty, minimum depth would be 0
        if root is None: 
            return 0 

        # If root is a leaf node, minimum depth would be 1
        if root.left is None and root.right is None: 
            return 1

        # If left subtree is None, find minimum depth in right subtree 
        if root.left is None: 
            return self.minimumDepth(root.right)+1

        # If right subtree is None, find minimum depth in left subtree 
        if root.right is None: 
            return self.minimumDepth(root.left) +1 

        # Get the minimum depths of left and right subtrees and add 1 for current level.
        return min(self.minimumDepth(root.left), self.minimumDepth(root.right)) + 1

    def minimumDepth2(self, root):
        if root == None:
            return 0

        if root.left == None or root.right == None:
            return self.minimumDepth2(root.left) + self.minimumDepth2(root.right)+1

        return min(self.minimumDepth2(root.right), self.minimumDepth2(root.left))+1

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(4)
# tree.right = TreeNode(2)
# tree.right.right = TreeNode(3)
# tree.right.left = TreeNode(4)

temp = Solution()
print temp.minimumDepth(tree)
