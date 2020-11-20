# Link: https://leetcode.com/problems/clone-graph/discuss/937831/Python3-DFS-recursion-solution
# IsDone: 0
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        log = {}
        
        def clone(n):
            if n.val not in log:
                res = Node(n.val)
                log[res.val] = res
                for nei in n.neighbors:
                    res.neighbors.append(clone(nei))
            return log[n.val]
        return None if node is None else clone(node)