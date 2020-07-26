#

def findIntersectingNode(self, list1, list2):
	intersect = {}
	t = list1
	while None != t:
		intersect[t] = True
		t = t.get_next()

	# first duplicate is intersection
	t = list2
	while None != t:
		if None != intersect.get(t):
			return t
		t = t.get_next()
	return None
