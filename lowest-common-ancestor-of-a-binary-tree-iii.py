'''
L1650
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
Runtime: 89 ms, faster than 16.85% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree III.
Memory Usage: 18.4 MB, less than 61.73% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree III.
'''
def xprint(*args, **kwargs):
    return
    print("".join(map(str, args)), **kwargs)

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pll = []
        qll = []
        tp = p
        while tp != None:
            tq = q  
            xprint(f"{tp.val}")
            while tq != None:
                xprint(f"{tp.val}<>{tq.val}")
                if tp.val == tq.val:
                    xprint(f"{tp.val}")
                    return tp
                tq = tq.parent
            tp = tp.parent
        
