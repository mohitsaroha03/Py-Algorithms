''

def pathFinder(root, val, path, paths):
    if not root:
        return False
    
    if not root.left and not root.right:
        if root.data == val:
            path.append(root.data)
            paths.append(path)
            return True
        else:
            return False
    
    left = pathFinder(root.left, val - root.data, path + [root.data], paths)
    right = pathFinder(root.right, val - root.data, path + [root.data], paths)  # make sure it can be executed!
    return left or right


def hasPathWithSum(root, val):
    paths = []
    pathFinder(root, val, [], paths)
    print 'sum:', val
    print 'paths:', paths
