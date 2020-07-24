# isGFG: , Link: 
# IsDone: 0
def DLLtoBalancedBST(head):
	if(not head or not head.next): 
		return head
	temp = FindMiddleNode(head)  # Refer Linked Lists chapter for this function. 
	# We can use two-pointer logic to find the middle node
	p = head
	while(p.next != temp):
		p = p.next
	p.next = None
	q = temp.next
	temp.next = None
	temp.prev = DLLtoBalancedBST(head)
	temp.next = DLLtoBalancedBST(q)
	return temp
