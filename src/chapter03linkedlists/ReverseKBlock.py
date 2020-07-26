#

def reverseKBlock(self, head, k):
        temp = Node(0);
        temp.set_next(head)
        previous = temp
        while True:
            begin = previous.get_next()
            end = previous
            for i in range(0, k):
                end = end.get_next()
                if end == None:
                    return temp.get_next()
            nextBlock = end.get_next()
            self.reverseList(begin, end)
            previous.set_next(end)
            begin.set_next(nextBlock)
            previous = begin
        
def reverseList(self, start, end):
	alreadyReversed = start
	actual = start
	nextNode = start.get_next()
	while actual != end:
	    actual = nextNode
	    nextNode = nextNode.get_next()
	    actual.set_next(alreadyReversed)
	    alreadyReversed = actual
