# Link: https://www.youtube.com/watch?v=ycMaIp8ynpI
# https://www.geeksforgeeks.org/find-fractional-nk-th-node-linked-list/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
         
    def set_data(self, data):
        self.data = data
     
    def get_data(self):
        return self.data
     
    def set_next(self, next):
        self.next = next
         
    def get_next(self):
        return self.next
     
     
class LinkedList:
    def __init__(self):
        self.head = None
	
    def fractionalNode(self, k):
	fractionalNode = None
	currentNode = self.head
	i = 0
	if k <= 0:
		return None;
	
	while currentNode != None:
		if i % k == 0:
			if fractionalNode == None:
				fractionalNode = self.head
			else:
				fractionalNode = fractionalNode.get_next()		
		i = i + 1
		currentNode = currentNode.get_next()
		
	print (fractionalNode.get_data())
			
    def insertAtEnd(self, item):
        current = self.head
        if  current == None:
            node = Node(item)
            node.set_next(None)
            self.head = node
            return
            
        while current.get_next() != None:
            current = current.get_next()
             
        node = Node(item)
        current.set_next(node)

if __name__ == "__main__":
    linkedlst = LinkedList()
    linkedlst.insertAtEnd(1)
    linkedlst.insertAtEnd(2)
    linkedlst.insertAtEnd(3)
    linkedlst.insertAtEnd(4)
    linkedlst.insertAtEnd(5)
    linkedlst.insertAtEnd(6)
    linkedlst.insertAtEnd(7)
    linkedlst.insertAtEnd(8)
    linkedlst.insertAtEnd(9)
    linkedlst.insertAtEnd(10)
    linkedlst.fractionalNode(2)
    linkedlst.fractionalNode(3)
    linkedlst.fractionalNode(4)
