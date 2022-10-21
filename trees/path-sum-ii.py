"""
113. Path Sum II
https://leetcode.com/problems/path-sum-ii/
Medium

Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
Each path should be returned as a list of the node values, not node references.
A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:
Input: root = [1,2], targetSum = 0
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
approach
case1:empty node: 0
case2:leafnode: append path + if curr_sum == tgt_sum add to res + pop curr_elm
case3:nested node: append path and pop curr_elm while unwinding
T:O(n)
S:O(n)
"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def helper(root, curr_sum, tgt_sum, tpath, res, lvl=0):
            if root is None:             # case 1 : empty node
                return []
            curr_sum += root.val
            tpath.append(root.val)
            # print(f"{' '*lvl}{curr_sum} += {root.val} tp:{tpath}")
            
            if root.left is None and root.right is None:# case 2: leaf node
                if curr_sum == tgt_sum:
                    res.append(tpath.copy())
                    # print(f"{' '*lvl}matched {tgt_sum} with v:{root.val} tp: {tpath} res:{res}")
                if tpath: 
                    _ = tpath.pop()
                #     print(f"{' '*lvl}at {root.val} popping {_}")
                # else:
                #     print(f"{' '*lvl}at {root.val} nothing to pop!")
                return      
                
            # case 3 : nested node
            helper(root.left, curr_sum, tgt_sum, tpath, res, lvl+1)
            helper(root.right, curr_sum, tgt_sum, tpath, res, lvl+1)
            _ = tpath.pop()
            # print(f"{' '*lvl}backtrack pop {root.val} post popping {_} tp:{tpath} ")
            
        tpath, res = [], []
        helper(root, 0, targetSum, tpath, res)
        return res
