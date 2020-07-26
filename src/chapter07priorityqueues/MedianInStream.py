# Link: 
# IsDone: 0
class streamMedian: 
	def __init__(self): 
		self.minHeap, self.maxHeap = [], [] 
		self.n = 0   
	def insert(self, num): 
		if self.n % 2 == 0: 
			heapq.heappush(self.maxHeap, -1 * num) 
			self.n += 1 
			if len(self.minHeap) == 0: 
				return 
			if -1 * self.maxHeap[0] > self.minHeap[0]: 
				toMin = -1 * heapq.heappop(self.maxHeap) 
				toMax = heapq.heappop(self.minHeap) 
				heapq.heappush(self.maxHeap, -1 * toMax) 
				heapq.heappush(self.minHeap, toMin) 
			else: 
				toMin = -1 * heapq.heappushpop(self.maxHeap, -1 * num) 
				heapq.heappush(self.minHeap, toMin) 
				self.n += 1   
	def getMedian(self): 
		if self.n % 2 == 0: 
			return (-1 * self.maxHeap[0] + self.minHeap[0]) / 2.0 
		else: 
			return -1 * self.maxHeap[0]
