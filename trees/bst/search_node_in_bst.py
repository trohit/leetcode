"""
Problem
  
Search A Node In Binary Search Tree
Find whether a node with a given value is present in a given binary search tree or not.
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
# T:O(h) where h is height of BST. in a balanced BST, h = logn
# S:O(1)
def search_node_in_bst(root, value):
    """
    Args:
     root(BinaryTreeNode_int32)
     value(int32)
    Returns:
     bool
    """
    # Write your code here.
    curr = root
    while curr:
        v = curr.value
        # print(f"v:{v}")
        if curr.value < value:
            # print(">")
            curr = curr.right
        elif curr.value > value:
            # print("<")
            curr = curr.left
        else: # must be eq
            # print("found")
            return True
    return False
