"""
112. Path Sum
https://leetcode.com/problems/path-sum/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
T:O(n)
S:O(n) worst case, O(logn) best case if balanced tree
start DFS from root until we hit leafnode.
keep subtracting from tgt_sum along the way
foll cases arise
case 1 : empty tree, in which case pgm says we should return false
case 2 : leaf node, just compare, if tgt_sum is 0, then its what we need
case 3 : nested intermediate node, delegate left and right, if any is True then ret True 
"""
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(root, tgt_sum):
            # case 1 empty node / base case
            if root is None:
                return False
                
            tgt_sum -= root.val
            # print(f"sub {root.val} = {tgt_sum}")
            # case 2: leaf node
            if root.left is None and root.right is None:
                if tgt_sum == 0:
                    # print(f"tgt_sum:{tgt_sum}")
                    return True
                return False 
            
            # case 3: nested intermediate node
            lr = helper(root.left, tgt_sum)
            rr = helper(root.right, tgt_sum)
            # print(f"lr:{lr} rr:{rr}")
            if lr is True or rr is True:
                return True
            return False
        
        res = helper(root, targetSum)
        return res
                
            
            
