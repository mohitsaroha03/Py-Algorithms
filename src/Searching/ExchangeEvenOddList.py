# Link: 
# IsDone: 0
def exchangeEvenOddList(head):
	# initializing the odd and even list headers
	oddList = evenList = None

	# creating tail variables for both the list
	oddListEnd = evenListEnd = None    
	itr = head	

	if(head == None):
		return
	else:
		while(itr != None):
			if(itr.data % 2 == 0):
				if(evenList == NULL):
					# first even node 
					evenList = evenListEnd = itr
				else:
					# inserting the node at the end of linked list                        
					evenListEnd.next = itr                           
					evenListEnd = itr
			else:
				if(oddList == NULL):
					# first odd node 
					oddList = oddListEnd = itr
				else:
					# inserting the node at the end of linked list
					oddListEnd.next = itr                          
					oddListEnd = itr
		itr = itr.next
	evenListEnd.next = oddList
	return head
