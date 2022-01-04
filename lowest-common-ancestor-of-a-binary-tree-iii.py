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
        
'''
Option - 2
Better runtime : uses a set to check for dup elements and reduces O(m*n) to O(m+n) 
Space: O(m)
Time : O(m+n*O(1)) = O(m+n)
Runtime: 72 ms, faster than 54.26% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree III.
Memory Usage: 18.6 MB, less than 34.98% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree III.
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
        pll = set()
        while p != None:
            xprint(f"{p.val}")
            pll.add(p)
            p = p.parent

        while q != None:
            xprint(f"{q.val}")
            if q in pll:
                return q
            q = q.parent

            
'''
Option - 3 : Uses 2 pointer method like the same method used to find intersection of linkedlists.
Runtime: 68 ms, faster than 76.61% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree III.
Memory Usage: 18.4 MB, less than 61.73% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree III.
say len(p) = 3, len(q) = 5
say last 2 nodes are common
a1--------->
(p)        \
            -> c4 ->c5
(q)        /
b1->b2->b3
so start both pointers at the head of p1 and q1
after moving 3 nodes, p1 hits the end. then make p1 point to q.(b1)
after moving 5 nodes, p2 hits the end. then make it point to p.(a1)

at some point both of them will have traversed the same number of nodes.
Space: O(1)
Time : O(m+n)
'''
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a = p
        b = q
        while a != b:
            a = q if a == None else a.parent
            b = p if b == None else b.parent    
        return a
    
