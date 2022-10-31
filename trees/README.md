# TREES
```
    A
  +-^-+
  B   C
  | +-+-+
  D E F G
```
bfs:
    abcdefg
dfs:
    abdcefg
## Binary Tree
 - Tree with at max 2 child nodes
Types of Binary tree traversal: DFS and BFS
![formula](https://github.com/trohit/leetcode/blob/main/images/bfs_versus_dfs.PNG)
![formula](https://github.com/trohit/leetcode/blob/main/images/traversal_detail.PNG)

Types of Tree Traversal
https://en.wikipedia.org/wiki/Tree_traversal
 - DFS 
    - Uses a stack LIFO
    - Types of DFS traversal
    - (N)ode, (L)eft, (R)ight
      - pre - NLR  
      - in - LNR
      - post - LRN
      - rev pre-order - NRL 
      - rev in-order - RNL
      - rev post-order - RLN
 - BFS
    - Types of BFS Traversal
       - Level order traversal: prints all nodes level by level
       - Uses a queue FIFO
       - for lvl order traversal, maintain lvl specific qs or use a count  
- time complexity: total time taken wrt input size
- space complexity: extra space taken wrt input size
    - input (usually not considered)
    - auxiliary (includes stack + local vars)
    - output (incl result arr)


------------
## DFS
- DFS 
    - Uses a stack LIFO
    - Types of DFS traversal
    - (N)ode, (L)eft, (R)ight
      - pre - NLR  
      - in - LNR
      - post - LRN
      - rev pre-order - NRL 
      - rev in-order - RNL
      - rev post-order - RLN
```
      1
  +---^---+
  2       3
+-^-+   
4   5
pre(slr) :12453
in(lsr)  :42513
post(lrs):45231

      *
  +---^---+
  +       c
+-^-+   
a   b
pre(slr): *+abc
```
![formula](https://github.com/trohit/leetcode/blob/main/images/dfs_and_bfs.PNG)

```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
T:O(n) as each node is visited exactly once
S:O(n) as each node i sstored in 
where n is the number of nodes
"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def preorder(node, res)->None:
            # NLR
            if node is None:
                return
            res.append(node.val)
            preorder(node.left, res)
            preorder(node.right, res)
        # driver        
        preorder(root, res)
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder - LNR
        res = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def postOrder(node):
            # LRN
            if node is None: return
            postOrder(node.left)
            postOrder(node.right)
            res.append(node.val)
        postOrder(root)
        # print(res)
        return res
```       
------------
## BFS

BFS level order traversal
![formula](https://github.com/trohit/leetcode/blob/main/images/bfs_lvl_order.PNG)

------------

# Related leetcode probs

https://leetcode.com/problems/binary-tree-level-order-traversal/

https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
       
https://leetcode.com/problems/n-ary-tree-level-order-traversal/

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

https://leetcode.com/problems/binary-tree-right-side-view/
