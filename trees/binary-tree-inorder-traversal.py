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

"""
# iter version: https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
#               https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/
#               https://www.educative.io/answers/how-to-perform-an-iterative-inorder-traversal-of-a-binary-tree
#               
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # LNR 1,3,2
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inOrder(root):
            # Set current to root of binary tree
            current, stack, res = root, [], [] # initialize stack
            while True:
                # Reach the left most Node of the current Node
                if current is not None:
                    # Place pointer to a tree node on the stack 
                    # before traversing the node's left subtree
                    stack.append(current)
                    current = current.left 
                # BackTrack from the empty subtree and visit the Node
                # at the top of the stack; however, if the stack is 
                # empty you are done
                elif(stack):
                    current = stack.pop()
                    res.append(current.val)
                    #  Now, it's right subtree's turn
                    current = current.right 
                else:
                    break
            print(f"res:{res}")   
            return res
        
        # driver
        res = inOrder(root)
        return res
            
"""
