# Link: https://www.geeksforgeeks.org/given-an-array-of-numbers-arrange-the-numbers-to-form-the-biggest-number/
# https://leetcode.com/problems/largest-number/discuss/802170/Python-Easy-Solution
# https://leetcode.com/problems/largest-number/discuss/769614/python-quick-and-simple-solution-with-comments
# https://leetcode.com/problems/largest-number/discuss/769039/Python-3-custom-comparator-at-least-80
# Python3 Program to get the maximum 
# possible integer from given array 
# of integers... 


# custom comparator to sort according 
# to the ab, ba as mentioned in description 
def comparator(a, b): 
	ab = str(a) + str(b) 
	ba = str(b) + str(a) 
	print ab, ba
	return ((int(ba) > int(ab)) - (int(ba) < int(ab))) 
	
def myCompare(mycmp): 
	
	# Convert a cmp= function into a key= function 
	class K(object): 
		def __init__(self, obj, *args): 
			self.obj = obj 
		def __lt__(self, other): 
			return mycmp(self.obj, other.obj) < 0
		def __gt__(self, other): 
			return mycmp(self.obj, other.obj) > 0
		def __eq__(self, other): 
			return mycmp(self.obj, other.obj) == 0
		def __le__(self, other): 
			return mycmp(self.obj, other.obj) <= 0
		def __ge__(self, other): 
			return mycmp(self.obj, other.obj) >= 0
		def __ne__(self, other): 
			return mycmp(self.obj, other.obj) != 0
	return K 
# driver code 
if __name__ == "__main__": 
	a1 = [54, 546, 548, 60, ] 
	a = [1, 3, 2, 4, ] 
	oj = myCompare(comparator)
	sorted_array = sorted(a, key=oj) 
	number = "".join([str(i) for i in sorted_array]) 
	print(number) 