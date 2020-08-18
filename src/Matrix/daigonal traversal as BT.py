# https://www.techiedelight.com/print-diagonal-traversal-binary-tree/
# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Recursive function to do a pre-order traversal of the tree and
# fill the dictionary with diagonal elements
def printDiagonal(node, diagonal, dict):

    # base case: empty tree
    if node is None:
        return

    # insert current node in current diagonal
    dict.setdefault(diagonal, []).append(node.data)

    # recur for left subtree by increasing diagonal by 1
    printDiagonal(node.left, diagonal + 1, dict)

    # recur for right subtree with same diagonal
    printDiagonal(node.right, diagonal, dict)


# Function to print the diagonal elements of given binary tree
def printDiagonalElements(root):

    # create an empty multi-dict to store diagonal element in every slope
    dict = {}

    # do pre-order traversal of the tree and fill the dictionary
    printDiagonal(root, 0, dict)

    # traverse the dictionary and print diagonal elements
    for value in dict.values():
        print(value)


if __name__ == '__main__':

    """ Construct below tree
               1
             /   \
            /     \
          2        3
         /        /  \
        /        /    \
       4        5      6
               / \
             /    \
            7      8
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    printDiagonalElements(root)
