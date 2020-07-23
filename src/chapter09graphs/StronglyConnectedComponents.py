# isGFG: , Link: 
# IsDone: 0
def stronglyConnectedComponents(G):
    indexCounter = [0]
    stack = []
    lowLinks = {}
    index = {}
    result = []   
    def strongConnect(node):
        # set the depth index for this node to the smallest unused index
        index[node] = indexCounter[0]
        lowLinks[node] = indexCounter[0]
        indexCounter[0] += 1
        stack.append(node)
    
        # Consider successors of `node`
        try:
            successors = G[node]
        except:
            successors = []
        for successor in successors:
            if successor not in lowLinks:
                # Successor has not yet been visited; recurse on it
                strongConnect(successor)
                lowLinks[node] = min(lowLinks[node], lowLinks[successor])
            elif successor in stack:
                # the successor is in the stack and hence in the current strongly connected component (SCC)
                lowLinks[node] = min(lowLinks[node], index[successor])
        
        # If `node` is a root node, pop the stack and generate an SCC
        if lowLinks[node] == index[node]:
            connectedComponent = []
            
            while True:
                successor = stack.pop()
                connectedComponent.append(successor)
                if successor == node: break
            component = tuple(connectedComponent)
            # storing the result
            result.append(component)
    
    for node in G:
        if node not in lowLinks:
            strongConnect(node)
    
    return result
