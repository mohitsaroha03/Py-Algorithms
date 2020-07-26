#

def mergeTwoSortedLists(self, list1, list2):
	temp = Node(0)
	pointer = temp
	while list1 != None and list2 != None:
	    if list1.get_data() < list2.get_data():
		pointer.set_next(list1)
		list1 = list1.get_next()
	    else:
		pointer.set_next(list2)
		list2 = list2.get_next()
	    pointer = pointer.get_next()
	if list1 == None:
	    pointer.set_next(list2)
	else:
	    pointer.set_next(list1)
	return temp.get_next()
