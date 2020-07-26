# Link: 
# IsDone: 0
# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.data = x
		self.next = None

def Qsort(first, last):
	lesHEAD = lesTAIL = None
	equHEAD = equTAIL = None
	larHEAD = larTAIL = None
	current = first
	if(current == None):
		return
	pivot = current.data
	Append(current, equHEAD, equTAIL)
	while (current != None):
		info = current.data
		if(info < pivot):
			Append(current, lesHEAD, lesTAIL)
		elif(info > pivot):
			Append(current, larHEAD, larTAIL)
		else:
			Append(current, equHEAD, equTAIL)
	
	Quicksort(lesHEAD, lesTAIL)
	Quicksort(larHEAD, larTAIL)
	Join(lesHEAD, lesTAIL, equHEAD, equTAIL)
	Join(lesHEAD, equTAIL, larHEAD, larTAIL)
	first = lesHEAD
	last = larTAIL
