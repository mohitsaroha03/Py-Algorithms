# isGFG: , Link: 
# IsDone: 0
def lca(root, alpha, beta):
    if not root: return None
    if root.value == alpha or root.value == beta: return root
    left = lca(root.left, alpha, beta)
    right = lca(root.right, alpha, beta)
    if left and right: 
        # alpha & beta are on both sides
        return root
    else: 
        # EITHER alpha/beta is on one side 
        # OR alpha/beta is not in L&R subtrees
        return left if left else right
