"""
https://leetcode.com/problems/binary-tree-preorder-traversal
144. Binary Tree Preorder Traversal
Easy
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

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
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # slr
        res = []
        st = []
        if not root:# base case
            return
        st.append(root)
        while st:
            node =  st.pop()
            if node:
                # print(f"n:{node.val}")
                res.append(node.val)
                # pre - slr
                st.append(node.right)
                st.append(node.left)
        return res
        
 """
 # iterative implementation follows
 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # NLR
        if root is None:
            return []
        st, out = [root], [] # using a list as a stack
        while st:
            n = st.pop()
            # print(f"{n.val}")
            out.append(n.val)
            if n.right: # push left after right when we pop stack, left gets traversed first
                  st.append(n.right)
            if n.left:
                  st.append(n.left)
        return out
        
"""
