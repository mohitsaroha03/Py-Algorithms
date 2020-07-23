# isGFG: , Link: 
# IsDone: 0
class TreeNode:
     def __init__(self, data):
         self.val = data
         self.left = None
         self.right = None
class Solution:
	def buildTree(self, preorder, inorder):
		if not inorder: 
			return None  # inorder is empty
			root = TreeNode(preorder[0])
			rootPos = inorder.index(preorder[0])
			root.left = self.buildTree(preorder[1 : 1 + rootPos], inorder[ : rootPos])
			root.right = self.buildTree(preorder[rootPos + 1 : ], inorder[rootPos + 1 : ])
		return root
		
class Solution2:
    def buildTree(self, preorder, inorder):
        return self.buildTreeRec(preorder, inorder, 0, 0, len(preorder))
        
    def buildTreeRec(self, preorder, inorder, indPre, indIn, element):
        if element == 0:
            return None
        solution = TreeNode(preorder[indPre])
        numElementsLeftSubtree = 0;
        for i in range(indIn, indIn + element):
            if inorder[i] == preorder[indPre]:
                break
            numElementsLeftSubtree += 1
        solution.left = self.buildTreeRec(preorder, inorder, indPre + 1, indIn, numElementsLeftSubtree)
        solution.right = self.buildTreeRec(preorder, inorder, indPre + numElementsLeftSubtree + 1, indIn + numElementsLeftSubtree + 1, element - 1 - numElementsLeftSubtree)
        return solution		
