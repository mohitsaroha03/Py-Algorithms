# isGFG: , Link: 
# IsDone: 0
def sumNumbers(self, root):
	if not root:
		return 0
	current = 0
	sum = [0]
	self.printPathsRecur(root, current, sum)
	return sum[0]
	
def printPathsRecur(self, root, current, sum):
	if not root:
		return
	current = current * 10 + root.data
	if not root.left and not root.right:
		sum[0] += current
		return

	self.printPathsRecur(root.left, current, sum)
	self.printPathsRecur(root.right, current, sum)
