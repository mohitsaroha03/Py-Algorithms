# isGFG: , Link: 
# IsDone: 0
def largestRectangleArea(self, height):
	stack = []; i = 0; maxArea = 0
	while i < len(height):
	    if stack == [] or height[i] > height[stack[len(stack) - 1]]:
		stack.append(i)
	    else:
		curr = stack.pop()
		width = i if stack == [] else i - stack[len(stack) - 1] - 1
		maxArea = max(maxArea, width * height[curr])
		i -= 1
	    i += 1
	while stack != []:
	    curr = stack.pop()
	    width = i if stack == [] else len(height) - stack[len(stack) - 1] - 1
	    maxArea = max(maxArea, width * height[curr])
	return maxArea
