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
     
     
BFS level order traversal
![formula](https://github.com/trohit/leetcode/blob/main/images/bfs_lvl_order.PNG)


       
