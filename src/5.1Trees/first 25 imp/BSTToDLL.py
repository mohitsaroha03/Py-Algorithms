# isGFG: 0 , Link: https://www.techiedelight.com/place-convert-given-binary-tree-to-doubly-linked-list/
# IsDone: 1
# Data structure to store a Binary Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Function to print given doubly linked list
def printDLL(head):

    curr = head
    while curr:
        print curr.data
        curr = curr.right


# Function to in-place convert given Binary Tree to a Doubly Linked List

# root -> current node
# head -> head of the doubly linked list
# prev -> previous processed node

# """ Construct below tree
#               1
#            /     \
#           2       3
#          / \     / \
#         4   5   6   7
#     """

def convert(curr, head, prev):

    # base case: tree is empty
    if curr is None:
        return head, prev

    # recursively convert left subtree first
    head, prev = convert(curr.left, head, prev)

    # adjust pointers
    if prev:

        # set current node's left child to prev
        curr.left = prev

        # make prev's right child as curr
        prev.right = curr

    # if prev is None, then update head of DLL as this is first node in inorder
    else:
        head = curr

    # after current node is visited, update previous pointer to current node
    prev = curr

    # recursively convert right subtree
    return convert(curr.right, head, prev)


# In-place convert given Binary Tree to a Doubly Linked List
def convertToDDL(root):

    # prev - keep track of previous processed node in inorder traversal
    prev = None

    # convert above binary tree to DLL (using inorder traversal)
    head, prev = convert(root, root, prev)
    return head


if __name__ == '__main__':

    """ Construct below tree
              1
           /     \
          2       3
         / \     / \
        4   5   6   7
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    root = convertToDDL(root)

    # root is now head of doubly linked list

    # print list
    printDLL(root)
