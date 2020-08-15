# Link: https://www.w3resource.com/python-exercises/heap-queue-algorithm/python-heapq-exercise-16.php
# https://www.youtube.com/watch?v=6N6QQpoU7H4
# TODO: https://www.geeksforgeeks.org/connect-n-ropes-minimum-cost/
# TODO: https://www.geeksforgeeks.org/merge-k-sorted-linked-lists-set-2-using-min-heap/
import heapq
class Median_Finder:
    
    def __init__(self):
        #initialize data structure
        self.max_heap = []
        self.min_heap = []
        

    def add_Number(self, num):
        #type num: int, rtype: void
        if not self.max_heap and not self.min_heap:
            heapq.heappush(self.min_heap, num)
            return 
        if not self.max_heap:
            if num > self.min_heap[0]:
                heapq.heappush(self.max_heap, heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, num)
            return
        if len(self.max_heap) == len(self.min_heap):
            if num < self.max_heap[0]:
                heapq.heappush(self.max_heap, num)
            else:
                heapq.heappush(self.min_heap, num)
        elif len(self.max_heap) > len(self.min_heap):
            if num < self.max_heap[0]:
                heapq.heappush(self.min_heap, heapq.heappop(self.max_heap))
                heapq.heappush(self.max_heap, num)
            else:
                heapq.heappush(self.min_heap, num)
        else:
            if num > self.min_heap[0]:
                heapq.heappush(self.max_heap, heapq.heappop(self.min_heap))
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, num)
        

    def find_Median(self):
        #rtype: float
        if len(self.max_heap) == len(self.min_heap):
            return (self.max_heap[0] + self.min_heap[0]) / 2
        elif len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        else:
            return self.min_heap[0] 
S = Median_Finder()
S.add_Number(1)
S.add_Number(2)
result = S.find_Median()
print(result)
S.add_Number(3)
result = S.find_Median()
print(result)
S.add_Number(4)
S.add_Number(5)
result = S.find_Median()
print(result)
