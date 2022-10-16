"""
112. Path Sum
https://leetcode.com/problems/path-sum/

Given the root of a binary tree and an integer targetSum, return true 
if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.
 
Constraints:
The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""
# T: O(n)
# S: O(n)
class Solution:
    # pre order traversal
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def hlpr(root, tsum, csum)-> bool:
            # base
            if root is None:
                return False
            #  inter
            csum += root.val    
            # print(f"root:{root.val} tsum:{tsum} csum:{csum}")
            if root.left is None and root.right is None:
                if csum == tsum:
                    # print(f"rt true")
                    return True
            l = hlpr(root.left, tsum, csum)
            if l : return l
            r = hlpr(root.right, tsum, csum)
            return l or r
            
        val = hlpr(root, targetSum, 0)
        return val
        
        
