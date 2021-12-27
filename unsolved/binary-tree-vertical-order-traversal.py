'''
L314
https://leetcode.com/problems/binary-tree-vertical-order-traversal/

Examplify

Ranges
Obs
Testcases
Algo: tried using dfs and +/- vertical order
Complexity: 

Fails at TC:
inp:[3,9,8,4,0,1,7,null,null,null,2,5]
op :[[4],[9,5],[3,0,1],[2,8],[7]]
exp:[[4],[9,5],[3,0,1],[8,2],[7]]

Need to try with BFS instead
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def xprint(*args, **kwargs):
    # return
    print("".join(map(str, args)), **kwargs)
    
def trav(root, tdd, h, vorder):
    min_span = -h
    max_span = h
    span=vorder
    # edge cases
    if root != None:
        xprint(f"nv:{root.val} tdd:{tdd} h:{h} {min_span}..{max_span} span:{span}")
    if root == None:
        xprint(f"none so returning tdd:{tdd} h:{h} {min_span}..{max_span}")
        return 
    else:#store based on span as key
        if span in tdd:
            ll = tdd[span]
            ll.append(root.val)
            # ll.sort()
            tdd[span] = ll
        else:
            tdd[span]= []
            tdd[span].append(root.val)
            xprint(f"stored at key:[{span}]->{root.val} ")
    trav(root.left, tdd, h+1,span-1)
    trav(root.right, tdd,h+1,span+1)
    
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        tdd = dict()
        trav(root, tdd, 0, 0)
        xprint(tdd)
        keys = list(tdd.keys())
        keys.sort()
        oll = []
        for i in keys:
            xprint(f"{tdd[i]}")
            oll.append(tdd[i])
        xprint(oll)
        return oll
