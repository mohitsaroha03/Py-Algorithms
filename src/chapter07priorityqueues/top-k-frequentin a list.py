# Link: https://www.geeksforgeeks.org/find-top-k-or-most-frequent-numbers-in-a-stream/
# https://leetcode.com/problems/top-k-frequent-elements/solution/
import heapq
from collections import Counter
def topKFrequent(nums, k): 
	# O(1) time 
	if k == len(nums):
		return nums
	
	# 1. build hash map : character and how often it appears
	# O(N) time
	count = Counter(nums)   
	# 2-3. build heap of top k frequent elements and
	# convert it into an output array
	# O(N log k) time
	return heapq.nlargest(k, count.keys(), key=count.get) 

print( topKFrequent([1,2,3,9,4,5,6,7,8,9], 3))