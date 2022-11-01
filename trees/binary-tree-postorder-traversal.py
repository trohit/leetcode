"""
https://leetcode.com/problems/binary-tree-postorder-traversal/
145. Binary Tree Postorder Traversal
Easy
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
"""
Approach: recursive uses the call stack as the stack itself
post order: LRN 
T:O(n) as each nodes gets visited once
S:O(n) as each node is stored once
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def postOrder(node):
            # LRN
            if node is None: return
            postOrder(node.left)
            postOrder(node.right)
            res.append(node.val)
        postOrder(root)
        # print(res)
        return res
