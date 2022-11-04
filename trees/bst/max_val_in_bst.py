"""
Problem
  
Maximum Valued Node In Binary Search Tree
Find the node with maximum value in a given binary search tree and return its value.
T:O(h) where h = [logn..n] logn if balnced BST else n
S:O(h)
"""
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def get_maximum_value(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    curr = root
    if not curr: return None
    while curr.right: curr = curr.right    
    return curr.value
