"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
94. Binary Tree Inorder Traversal
Easy
Given the root of a binary tree, return the inorder traversal of its nodes' values.
"""
"""
T:O(n)
S:O(n)
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder - LNR
        res = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        print(res)
        return res
