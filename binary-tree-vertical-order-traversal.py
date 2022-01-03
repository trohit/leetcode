'''
L314
https://leetcode.com/problems/binary-tree-vertical-order-traversal
Runtime: 36 ms, faster than 60.51% of Python3 online submissions for Binary Tree Vertical Order Traversal.
Memory Usage: 14.5 MB, less than 8.81% of Python3 online submissions for Binary Tree Vertical Order Traversal.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
dfs: 4, 
bfs: 3 9 20 15 7
ip: [3,9,8,4,0,1,7]
op: [[4],[9],[3,0,1],[8],[7]]

          3
        9    8
       4 0  1  7
op: 4 9 301 8 7
'''
def xprint(*args, **kwargs):
    return
    print("".join(map(str, args)), **kwargs)

import collections
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return
        colwise = collections.defaultdict(list)
        
        def dfs(root, row=0, col=0):
            nonlocal colwise
            if root == None:
                return
            dfs(root.left, row+1, col-1)
            xprint(f"{root.val}", end=",")
            colwise[col].append((row, root.val))
            xprint(f"[{col}][{row}]= {root.val}")
            dfs(root.right, row+1, col+1)

        dfs(root);xprint()
        xprint(colwise)
        ll = []
        keys = colwise.keys()
        sorted_keys = sorted(list(keys))
        for i in sorted_keys:
            colwise[i].sort(key=lambda x:x[0])
            lvl_ll = [col for (row, col) in colwise[i]]
            ll.append(lvl_ll)
        xprint(ll)
        return ll
