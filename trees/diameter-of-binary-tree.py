"""
https://leetcode.com/problems/diameter-of-binary-tree
543. Diameter of Binary Tree
Easy
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.


Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1  
 
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0
        def dfs(root):
            if not root: return 0
            l = dfs(root.left)  # longest_path of left chld
            r = dfs(root.right) # longest_path of right child           
            dia = max(l,r) + 1  # so the longest_path of this node is the longer of the 2 child paths + 1 
            self.max_dia = max(self.max_dia, l+r) # dia of the tree is the maximum longest path
            return dia
        # driver
        dfs(root)
        return self.max_dia
