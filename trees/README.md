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
Types of Binary tree traversal
 - DFS 
    - Uses a stack LIFO
    - Types of DFS traversal
      - pre - s, l, r
      - in - l, s, r
      - post - l, r, s
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
     
     
BFS level order traversal
![formula](https://github.com/trohit/leetcode/blob/main/images/bfs_lvl_order.PNG)


Related leetcode probs

https://leetcode.com/problems/binary-tree-level-order-traversal/

https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
       
https://leetcode.com/problems/n-ary-tree-level-order-traversal/

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

https://leetcode.com/problems/binary-tree-right-side-view/
