# Link: https://www.geeksforgeeks.org/connect-nodes-at-same-level-with-o1-extra-space/
# https://www.youtube.com/watch?v=OLvzM1ZcbtQ
# IsDone: 0
class newnode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nextRight = None


# This function returns the leftmost child of 
# nodes at the same level as p. This function 
# is used to getNExt right of p's right child 
# If right child of is None then this can also 
# be used for the left child 
def getNextRight(p):
    temp = p.nextRight

    # Traverse nodes at p's level and find
    # and return the first node's first child
    while (temp != None):
        if (temp.left != None):
            return temp.left
        if (temp.right != None):
            return temp.right
        temp = temp.nextRight

    # If all the nodes at p's level are
    # leaf nodes then return None
    return None


# Sets nextRight of all nodes of a tree
# with root as p 
def connect(p):
    temp = None

    if (not p):
        return

    # Set nextRight for root
    p.nextRight = None

    # set nextRight of all levels one by one
    while (p != None):
        q = p

        # Connect all childrem nodes of p and
        # children nodes of all other nodes
        # at same level as p
        while (q != None):

            # Set the nextRight pointer for
            # p's left child
            if (q.left):

                # If q has right child, then right
                # child is nextRight of p and we
                # also need to set nextRight of
                # right child
                if (q.right):
                    q.left.nextRight = q.right
                else:
                    q.left.nextRight = getNextRight(q)

            if (q.right):
                q.right.nextRight = getNextRight(q)

            # Set nextRight for other nodes in
            # pre order fashion
            q = q.nextRight

        # start from the first node
        # of next level
        if (p.left):
            p = p.left
        elif (p.right):
            p = p.right
        else:
            p = getNextRight(p)

        # Driver Code


if __name__ == '__main__':

    # Constructed binary tree is
    #	 10
    #	 / \
    #	 8	 2
    # /		 \
    # 3		 90
    root = newnode(10)
    root.left = newnode(8)
    root.right = newnode(2)
    root.left.left = newnode(3)
    root.right.right = newnode(90)

    # Populates nextRight pointer in all nodes
    connect(root)

    # Let us check the values of nextRight pointers
    print "Following are populated nextRight pointers in the tree + -1 is print d if there is no nextRight) \n"
    print "nextRight of", root.dat, "is"
    if root.nextRight:
        print root.nextRight.data
    else:
        print -1
    print "nextRight of", root.left.data, "is"
    if root.left.nextRight:
        print root.left.nextRight.data
    else:
        print -1
    print "nextRight of", root.right.data, "is"
    if root.right.nextRight:
        print root.right.nextRight.data
    else:
        print -1
    print "nextRight of", root.left.left.data, "is"
    if root.left.left.nextRight:
        print root.left.left.nextRight.data
    else:
        print -1
    print "nextRight of", root.right.right.data, "is"
    if root.right.right.nextRight:
        print root.right.right.nextRight.data
    else:
        print -1
