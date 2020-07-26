# Link: 
# IsDone: 0
def sumNumbers(self, root):
	if not root:
		return 0
	current = 0
	sum = [0]
	self.calSum(root, current, sum)
	return sum[0]
	
def calSum(self, root, current, sum):
	if not root:
		return
	current = current * 10 + root.data
	if not root.left and not root.right:
		sum[0] += current
		return

	self.calSum(root.left, current, sum)
	self.calSum(root.right, current, sum)
