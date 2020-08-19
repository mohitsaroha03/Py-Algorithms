# Link: https://www.geeksforgeeks.org/k-largestor-smallest-elements-in-an-array/
# https://www.techiedelight.com/find-kth-smallest-largest-element-bst/
# IsDone: 0
import heapq
class Heap:
	def __init__(self):
		self.heapList = [0]  # Elements in Heap
		self.size = 0  # Size of the heap
	def parent(self, index):
		"""
		Parent will be at math.floor(index/2). Since integer division
		simulates the floor function, we don't explicitly use it
		"""
		return index // 2
		
	def leftChildIndex(self, index):
		return 2 * index
		
	def rightChildIndex(self, index):
		return 2 * index + 1
		
	def leftChild(self, index):
		if 2 * index <= self.size:
			return self.heapList[2 * index ]
		return -1
		
	def rightChild(self, index):
		if 2 * index + 1 <= self.size :
			return self.heapList[2 * index + 1]
		return -1	

	def searchElement(self, itm):
		i = 1
		while (i <= self.size):
			if itm == self.heapList[i]:
				return i
			i += 1
	# Get Minimum for MinHeap
	def getMinimum(self):
	     if self.size == 0:
		  return -1
	     return self.heapList[1]

	def percolateDown(self, i):
	    while (i * 2) <= self.size:
		minimumChild = self.minimumChild(i)
		if self.heapList[i] > self.heapList[minimumChild]:
		    tmp = self.heapList[i]
		    self.heapList[i] = self.heapList[minimumChild]
		    self.heapList[minimumChild] = tmp
		i = minimumChild

	def minimumChild(self, i):
	    if i * 2 + 1 > self.size:
		return i * 2
	    else:
		if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
		    return i * 2
		else:
		    return i * 2 + 1

	def percolateUp(self, i):
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i // 2]:
				tmp = self.heapList[i // 2]
				self.heapList[i // 2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i // 2

	# Delete Minimum for MinHeap
	def deleteMin(self):
	    retval = self.heapList[1]
	    self.heapList[1] = self.heapList[self.size]
	    self.size = self.size - 1
	    self.heapList.pop()
	    self.percolateDown(1)
	    return retval

	def insert(self, k):
		self.heapList.append(k)
		self.size = self.size + 1
		self.percolateUp(self.size)

	def printHeap(self):
		print self.heapList[1:]
		
	    
def FindKthLargestEle(HOrig, k):
	count = 1
	HAux = Heap()
	itm = HOrig.getMinimum()
	HAux.insert(itm)
	if count == k:
		return itm		
	while (HAux.size >= 1):
		itm = HAux.deleteMin()
		count += 1
		if count == k:
			return itm
		else:
			if HOrig.rightChild(HOrig.searchElement(itm)) != -1:
				HAux.insert(HOrig.rightChild(HOrig.searchElement(itm)))
			if HOrig.leftChild(HOrig.searchElement(itm)) != -1:	
				HAux.insert(HOrig.leftChild(HOrig.searchElement(itm)))

HOrig = Heap()
# add some nonsense:
HOrig.insert(1)
HOrig.insert(20)
HOrig.insert(5)
HOrig.insert(100)
HOrig.insert(1000)
HOrig.insert(12)
HOrig.insert(18)
HOrig.insert(16)

print FindKthLargestEle(HOrig, 6)
print FindKthLargestEle(HOrig, 3)

# https://medium.com/analytics-vidhya/how-to-find-k-th-smallest-largest-element-in-an-unsorted-array-4ab7015d802a
import heapq
def kthSmallest(arr, k):
    smallest = []
    for value in arr:
        if (len(smallest) < k):
            heapq.heappush(smallest, -value)
        else:
            heapq.heappushpop(smallest, -value)
    if (len(smallest) < k):
        return None
    return -smallest[0]

''' Python3 code for k largest elements in an array'''

def kLargest(arr, k): 
	# Sort the given array arr in reverse 
	# order. 
	arr.sort(reverse = True) 
	# Print the first kth largest elements 
	for i in range(k): 
		print (arr[i]) 

# Driver program 
arr = [1, 23, 12, 9, 30, 2, 50] 
# n = len(arr) 
k = 3
kLargest(arr, k) 