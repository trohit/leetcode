"""
https://leetcode.com/problems/delete-node-in-a-bst/
450. Delete Node in a BST
Medium
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.

Example 1:
Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bst_succ(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def bst_pre(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root.val
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # case 1 : empty tree        
        if not root: 
            return None
        # case 2: elm > root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        # case 3: elm < root
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: # node == root
            # case 4: todel is leaf node
            if root.left == root.right == None:
                root = None
            # case 5 : todel node has right child
            elif root.right:
                root.val = self.bst_succ(root)
                root.right = self.deleteNode(root.right, root.val)
            # case 6 : todel node has left child
            else: #if root.left:
                root.val = self.bst_pre(root)
                root.left = self.deleteNode(root.left, root.val)
        return root
                
