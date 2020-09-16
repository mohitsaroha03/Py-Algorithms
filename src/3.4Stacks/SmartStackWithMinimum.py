# Link: https://www.techiedelight.com/design-a-stack-which-returns-minimum-element-without-using-auxiliary-stack/
# https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
# https://www.geeksforgeeks.org/design-and-implement-special-stack-data-structure/
# IsDone: 0
# Reconsider: 1
# Class to make a Node 
from collections import deque


class MinStack:
	def __init__(self):

		# main stack to store elements
		self.s = deque()

		# variable to store minimum element
		self.min = None

	# Inserts a given element on top of the stack
	def push(self, x):

		if not self.s:
			self.s.append(x)
			self.min = x

		elif x > self.min:
			self.s.append(x)

		else:
			self.s.append(x - self.min)
			self.min = x

	# Removes top element from the stack and returns it
	def pop(self):

		if not self.s:
			print("Stack underflow!!")

		top = self.s[-1]
		if top < self.min:
			self.min = self.min - top
		self.s.pop()

	# Returns the minimum element from the stack in constant time
	def minimum(self):

		return self.min


if __name__ == '__main__':

	s = MinStack()

	s.push(6)
	print(s.minimum())

	s.push(7)
	print(s.minimum())

	s.push(5)
	print(s.minimum())

	s.push(3)
	print(s.minimum())

	s.pop()
	print(s.minimum())

	s.pop()
	print(s.minimum())