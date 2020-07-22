''

class Answer:
    def maxPathSum(self, root):
        self.maxValue = float("-inf")
        self.maxPathSumRec(root)
        return self.maxValue
    
    def maxPathSumRec(self, root):
        if root == None:
             return 0
        leftSum = self.maxPathSumRec(root.left)
        rightSum = self.maxPathSumRec(root.right)
        if leftSum < 0 and rightSum < 0:
            self.maxValue = max(self.maxValue, root.val)
            return root.val
        if leftSum > 0 and rightSum > 0:
            self.maxValue = max(self.maxValue, root.val + leftSum + rightSum)
        maxValueUp = max(leftSum, rightSum) + root.val
        self.maxValue = max(self.maxValue, maxValueUp)
        return maxValueUp
