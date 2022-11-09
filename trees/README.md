# TREES
- From graph point-of-view, a tree can also be defined as a directed acyclic graph which has N nodes and N-1 edges
- A tree is a frequently-used data structure to simulate a hierarchical tree structure.
  - A Binary Tree is one of the most typical tree structure. As the name suggests, a binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.

```
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8
pre :NLR:12435786 # https://www.techiedelight.com/preorder-tree-traversal-iterative-recursive/
in  :LNR:42175836 # https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/
post:LRN:42785631 # https://www.techiedelight.com/postorder-tree-traversal-iterative-recursive/
    '''
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
      - pre - NLR https://leetcode.com/problems/binary-tree-preorder-traversal/
      - in - LNR https://leetcode.com/problems/binary-tree-inorder-traversal/
      - post - LRN https://leetcode.com/problems/binary-tree-postorder-traversal
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

![formula](https://github.com/trohit/leetcode/blob/main/images/Preorder-Traversal.png)
![formula](https://github.com/trohit/leetcode/blob/main/images/Inorder-Traversal.png)
![formula](https://github.com/trohit/leetcode/blob/main/images/Postorder-Traversal.png)


## Recursive Traversal - preorder,inorder,postorder
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
### One liners
```
# Python 1-liner
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        return [] if not root else [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
```

### Iterative traversal - preorder,inorder,postorder
```
"""
      1
  +---^---+
  2       3
+-^-+   
4   5
pre(slr) :12453
in(lsr)  :42513
post(lrs):45231

- uses list as stack and 'append' to 'push' to stack
- in stack, both push and pop happen from the same end
"""
def preOrder(root) -> List[int]:# NLR
    if root is None:return []
    st, out = [root], [] # using a list as a stack
    while st:
        n = st.pop()
        out.append(n.val)
        # push left after right when we pop stack, left gets traversed first
        if n.right:st.append(n.right)
        if n.left:st.append(n.left)
    return out

def inOrder(root): #LNR
    curr, st, res = root, [], []
    while st or curr:
        if curr:
            st.append(curr)
            curr = curr.left 
        else:
            curr = st.pop()
            res.append(curr.val)
            curr = curr.right 
    return res

def postOrder(root)->List[int]:#LRN
    res, st = [], [root]
    while st:
        node = st[-1] # peek into stack
        if node.left:
            st.append(node.left)
            node.left = None
        elif node.right:
            st.append(node.right)
            node.right = None
        else:
            st.pop()
            res.append(node.value)
    return res
```
------------
## BFS

BFS level order traversal
![formula](https://github.com/trohit/leetcode/blob/main/images/bfs_lvl_order.PNG)

------------

# Related leetcode probs

- https://leetcode.com/problems/binary-tree-level-order-traversal/
- https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
- https://leetcode.com/problems/n-ary-tree-level-order-traversal/
- https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
- https://leetcode.com/problems/binary-tree-right-side-view/
- https://leetcode.com/problems/path-sum/
- https://leetcode.com/problems/path-sum-ii/
- https://leetcode.com/problems/diameter-of-binary-tree/
- https://leetcode.com/problems/diameter-of-n-ary-tree/


# Related links
- https://leetcode.com/explore/learn/card/data-structure-tree/
