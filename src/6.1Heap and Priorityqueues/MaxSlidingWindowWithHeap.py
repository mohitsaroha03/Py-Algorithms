# Link: https://leetcode.com/problems/sliding-window-maximum/
# solution:  https://leetcode.com/problems/sliding-window-maximum/discuss/65957/python-solution-with-detailed-explanation
# IsDone: 0
# convert -n to n for min sliding window
import heapq

class Solution:
    def maxSlidingWindow(self, nums, k) :
        pq = []
        res = []
        
        for i,n in enumerate(nums):
            if i+1 < k:
                heapq.heappush(pq, (-n, i))
            else:
                heapq.heappush(pq, (-n, i))
                x, idx = self.find_max(pq, i-k+1)
                res.append(-x)
                heapq.heappush(pq, (x, idx))
                
        return res
                
                
    def find_max(self, pq, start):
        while True:
            x, idx = heapq.heappop(pq)
            
            if idx >= start:
                return x, idx
s = Solution()
print s.maxSlidingWindow([5,4,3,14],2)
