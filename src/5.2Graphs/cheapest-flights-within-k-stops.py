# Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/929989/Python3-Dijkstra's-algo
# https://github.com/enggen/LeetCode/blob/master/Python/cheapest-flights-within-k-stops.py
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        adj = collections.defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        min_heap = [(0, src, K+1)]
        while min_heap:
            result, u, k = heapq.heappop(min_heap)
            if u == dst:
                return result
            if k > 0:
                for v, w in adj[u]:
                    heapq.heappush(min_heap, (result+w, v, k-1))
        return -1


# using BFS
# https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/937101/Python-Simple-BFS
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        cities = [[] for _ in range(n)]
        
        for u, v, w in flights:
            cities[u].append((v, w))
        
        queue = deque([(src, 0, 0)])
        costToDist = float("inf")
        
        while queue:
            city, accumulatedCost, numStops = queue.popleft()
            
            if city == dst:
                costToDist = min(costToDist, accumulatedCost)
                continue
            
            if numStops > K or accumulatedCost >= costToDist:
                continue
            
            for neighbouringCity, cost in cities[city]:
                queue.append((neighbouringCity, accumulatedCost + cost, numStops+1))
        
        return costToDist if costToDist < float("inf") else -1

