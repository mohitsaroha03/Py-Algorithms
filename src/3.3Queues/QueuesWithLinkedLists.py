# Link: https://www.geeksforgeeks.org/queue-linked-list-implementation/
# IsDone: 1

# A linked list (LL) node 
# to store a queue entry 
class Node: 
	
	def __init__(self, data): 
		self.data = data 
		self.next = None

# A class to represent a queue 

# The queue, front stores the front node 
# of LL and rear stores the last node of LL 
class Queue: 
	
	def __init__(self): 
		self.front = self.rear = None

	def isEmpty(self): 
		return self.front == None
	
	# Method to add an item to the queue 
	def EnQueue(self, item): 
		temp = Node(item) 
		# 10-20-30
		if self.rear == None: 
			self.front = self.rear = temp 
			return
		self.rear.next = temp 
		self.rear = temp 

	# Method to remove an item from queue 
	def DeQueue(self): 
		
		if self.isEmpty(): 
			return
		# 10-20-30
		temp = self.front 
		self.front = temp.next

		if(self.front == None): 
			self.rear = None

# Driver Code 
if __name__== '__main__': 
	q = Queue() 
	q.EnQueue(10) 
	q.EnQueue(20) 
	q.EnQueue(21) 
	q.DeQueue() 
	q.DeQueue() 
	q.EnQueue(30) 
	q.EnQueue(40) 
	q.EnQueue(50) 
	q.DeQueue() 
	print("Queue Front " + str(q.front.data)) 
	print("Queue Rear " + str(q.rear.data)) 
	
