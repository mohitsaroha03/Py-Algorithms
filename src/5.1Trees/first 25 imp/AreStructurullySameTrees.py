# Link: https://www.geeksforgeeks.org/check-if-two-trees-have-same-structure/
# # IsDone: 1

def areStructurullySameTrees(root1, root2):
    if root1 == None and root2 == None:
        return 1
    if root1 is not None and root2 is not None:
        return 1
    if root1 is None or root2 is None:
        return 0
    return areStructurullySameTrees(root1.left, root2.right) and areStructurullySameTrees(root1.right, root2.left)
