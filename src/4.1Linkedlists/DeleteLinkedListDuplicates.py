#

# Mohit: ye comparison sirf current node ka next node ka kr rha hai
# 1--2--2--3--4--5--6--7--8--6--9--8
def deleteLinkedListDuplicates(self):
	current = self.head; # 1
	while current != None and current.next != None:
	    if current.get_data() == current.get_next().get_data():
		current.set_next(current.get_next().get_next())
	    else:
		current = current.get_next()
	return head
