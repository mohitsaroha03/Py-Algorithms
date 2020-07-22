''

def rangePrinter(root, K1, K2): 
	if not root: 
		return 
	if K1 <= root.get_data() <= K2: 
		print(root.get_data())
	if root.get_data() < K1: 
		return rangePrinter(root.getRight(), K1, K2) 
	if root.get_data() > K2: 
		return rangePrinter(root.getLeft(), K1, K2)


import Queue
def rangePrinter(root):
	if root is None:
		return

	q = Queue.Queue()
	q.put(root)
	temp = None

	while not q.empty():
		temp = q.get()  # dequeue FIFO
		if K1 <= root.get_data() <= K2: 
			print(root.get_data())
		if temp.getLeft() is not None and temp.get_data() >= K1:
			q.put(temp.getLeft())
		if temp.getRight() is not None and temp.get_data() <= K2:
			q.put(temp.getRight())	

	
