# Link: https://www.techiedelight.com/floor-ceil-bst-iterative-recursive/
# IsDone: 1

# Python program to find floor and ceil of a given value in BST


# Data structure to store a Binary Search Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Recursive function to insert a key into BST
def insert(root, key):

    # if the root is None, create a node and return it
    if root is None:
        return Node(key)

    # if given key is less than the root node, recur for left subtree
    if key < root.data:
        root.left = insert(root.left, key)

    # if given key is more than the root node, recur for right subtree
    else:
        root.right = insert(root.right, key)

    return root


# Recursive function to find floor and ceil of a given key in a BST
def findFloorCeil(root, floor, ceil, key):

    while root:
        # if node with key's value is found, both floor and ceil is equal
        # to the current node
        if root.data == key:
            floor = ceil = root
            break

        # if given key is less than the root node, visit left subtree
        elif key < root.data:
            # update ceil to current node before visiting left subtree
            ceil = root
            root = root.left

        # if given key is more than the root node, visit right subtree
        else:
            # update floor to current node before visiting right subtree
            floor = root
            root = root.right

    return floor, ceil


if __name__ == '__main__':

    """ Construct below tree
               8
             /   \
            /     \
           4       10
          / \     /  \
         /   \   /    \
        2     6 9      12
    """

    keys = [2, 4, 6, 8, 9, 10, 12]

    root = None
    for key in keys:
        root = insert(root, key)

    # find Ceil and Floor for each key
    for i in range(15):

        floor, ceil = findFloorCeil(root, None, None, i)

        print(i)
        print("Floor is", floor.data if floor else None)
        print("Ceil is", ceil.data if ceil else None)
