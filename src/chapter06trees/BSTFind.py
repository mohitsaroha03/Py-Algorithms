# Link: https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
# IsDone: 1
# Search the key from node, iteratively

def Find(self, root, data):
    currentNode = root
    while currentNode:
        if data == currentNode.get_data():
            return currentNode
        if data < currentNode.get_data():
            currentNode = currentNode.getLeft()
        else:
            currentNode = currentNode.getRight()
    return None
