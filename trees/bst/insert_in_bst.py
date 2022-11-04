"""
Problem
Insert In BST
Given an array of numbers, build a binary search tree(BST) by inserting the values sequentially inside an initially empty BST.

Example
{
"values": [7, 5, 9]
}
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
# T:O(h) where h = n but if its a balanced BST then h=logn where n is total num of nodes
# S:O(1) for the auxiliary space as a const amt of mem is used
def build_a_bst(values):
    """
    Args:
     values(list_int32)
    Returns:
     BinaryTreeNode_int32
    """
    def helper(node, value):
        newNode = BinaryTreeNode(value)
        if node is None:
            return newNode
        prev = None
        curr = node
        while curr is not None:
            prev = curr
            if curr.value > value:
                curr = curr.left
            else:
                curr = curr.right
        if prev.value > value:
            prev.left = newNode
        else:
            prev.right = newNode
        return root
    
    root = None
    for v in values:
        root = helper(root, v)
    return root
