#

def getIntersectionNode(self, list1, list2):
	currentList1, currentList2 = list1, list2
	list1Len, list2Len = 0, 0
	while currentList1 is not None:
	    list1Len += 1
	    currentList1 = currentList1.next
	while currentList2 is not None:
	    list2Len += 1
	    currentList2 = currentList2.next
	currentList1, currentList2 = list1, list2
	if list1Len > list2Len:
	    for i in range(list1Len - list2Len):
		currentList1 = currentList1.next
	elif list2Len > list1Len:
	    for i in range(list2Len - list1Len):
		currentList2 = currentList2.next
	while currentList2 != currentList1:
	    currentList2 = currentList2.next
	    currentList1 = currentList1.next
	return currentList1
