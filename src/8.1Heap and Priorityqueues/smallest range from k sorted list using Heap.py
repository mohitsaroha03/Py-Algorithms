# Link: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/discuss/?currentPage=1&orderBy=hot&query=
# https://www.geeksforgeeks.org/find-smallest-range-containing-elements-from-k-lists/
# IsDone: 0
# class Solution(object):
import heapq
def smallestRange(nums):
    """
    :type nums: List[List[int]]
    :rtype: List[int]
    """
    h = []
    start, end = float('inf'), float('-inf')
    for i in range(len(nums)):
        heapq.heappush(h, [nums[i][0], i, 0])
        start = min(start, nums[i][0])
        end = max(nums[i][0], end)   

    res = [start, end]
    max_end = end
    while h:
        val, list_index, index = heapq.heappop(h)
        if index + 1 >= len(nums[list_index]):
            return res
        index = index + 1
        heapq.heappush(h, [nums[list_index][index], list_index, index])
        new_start = h[0][0]
        max_end = max(max_end, nums[list_index][index])
        if max_end - new_start < res[1] - res[0]:
            res = [new_start, max_end]
    return res
Lst = [ 
    [4, 7, 9,], 
    [0, 8, 10,], 
    [6, 12, 16,] 
    ] 
print smallestRange(Lst)
