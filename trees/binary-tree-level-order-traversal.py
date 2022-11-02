"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
102. Binary Tree Level Order Traversal
Medium
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
"""
Approach:
0. Base case: if root is empty, just return empty q.
1. Use BFS and a q
2. at each level, iterate through nodes in the q and stash their children into the q
3. To track the # of nodes at each level, keep track of len(q) which initially maybe 1.

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
    def disp(self, q):
        while q:
            print(f"{root.val}", end=',')
            root = root.next
                  
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        q = []
        q.append(root)
        lvl = 1

        res.append([root.val])
        while q:
            # self.disp(q)
            cnt = len(q)
            # print(f"reset tq res:{res}")
            tq = [] # only consists of node vals
            while cnt:
                t = q.pop(0)
                # print(f"lvl:{lvl} cnt:{cnt} stash {t.val}'s nodes")
                if t.left:
                    q.append(t.left)
                    tq.append(t.left.val)
                if t.right:
                    q.append(t.right)
                    tq.append(t.right.val)
                # print(f"{cnt}--")
                cnt -= 1
            # print("eol")
            if tq:
                # print(f"res:{res} tq:{tq} ")
                res.append(tq[:])
                tq.clear()
            lvl += 1
            # print(f"q:{q}")
        print(res)
        return res
