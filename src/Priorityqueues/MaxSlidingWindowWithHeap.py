# Link: https://leetcode.com/problems/sliding-window-maximum/discuss/65957/python-solution-with-detailed-explanation
# IsDone: 0
import heapq as h
class Solution(object):
    def get_next_max(self, heap, start):
        while True:
            x,idx = h.heappop(heap)
            if idx >= start:
                return x*-1, idx
    
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        heap = []
        for i in range(k):
            h.heappush(heap, (nums[i]*-1, i))
        result, start, end = [], 0, k-1
        while end < len(nums):
            x, idx = self.get_next_max(heap, start)
            result.append(x)
            h.heappush(heap, (x*-1, idx)) 
            start, end = start + 1, end + 1
            if end < len(nums):
                h.heappush(heap, (nums[end]*-1, end))
        return result
