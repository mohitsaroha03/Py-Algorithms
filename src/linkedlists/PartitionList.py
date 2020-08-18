#

# Node of a Singly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class for defining a linked list   
class PartitionList(object):
    # initializing a list
    def __init__(self):
        self.length = 0
        self.head = None
    def partition(self, head, X):
        # lesser and greater are the two pointers used to create two list
        # lesser_head and greater_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        lesser = lesser_head = Node(0)
        greater = greater_head = Node(0)

        while head:
            # If the original list node is lesser than the given X, assign it to the lesser list.
            if head.data < X:
                lesser.next = head
                lesser = lesser.next
            else:
                # If the original list node is greater or equal to the given X, assign it to the greater list.
                greater.next = head
                greater = greater.next

            # move ahead in the original list
            head = head.next

        # Last node of "greater" list would also be ending node of the reformed list
        greater.next = None

        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        lesser.next = greater_head.next

        return lesser_head.next
