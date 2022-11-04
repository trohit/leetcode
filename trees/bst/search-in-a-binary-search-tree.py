"""
700. Search in a Binary Search Tree
Easy
You are given the root of a binary search tree (BST) and an integer val.
Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
If such a node does not exist, return null.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # T:O(h)
    # S:O(h)
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val:        
            # print("case 1 : empty or val")
            return root
        # print(f"root:{root.val}")
        if val < root.val:      
            # print("# case 2 : smaller")
            return self.searchBST(root.left, val)
        elif val > root.val:    
            # print("# case 3 : greater")
            return self.searchBST(root.right, val)

 
