# Backtracking

| backtracking type  | Total Number    | Mnemonic           | Eg.             |
| -------------------| --------------- |--------------------|-----------------| 
| Subsets            | O(2^n)          | to choose or !     | [], [1]         |
| Combinations       | n!/(n-k)! * n!  | n elms,k slots nCk | [1,2]           | 
| Permutations       | n!              | factorial          | [1,2],[2,1]     | 

Menomonic poems to remember max items
Subsets are twice as powerful exponentially
Combos are nCk
Perms are facts

![formula](https://github.com/trohit/leetcode/blob/main/images/backtracking.PNG)

## subsets
subsets: max items 2^n where n is the num of uniq items in the set.\
Time Complexity : O(n.2^n), as we can choose to take |take each of n elms and at the leaf node we will have 2^n items of (len n) each\
Space Complexity: O(n), as the total mem will be the height of the tree 1->2->3

at every elm, have a choice: to include or not to include

Watch Neetcode video: https://neetcode.io/courses/advanced-algorithms/11
[![Watch the subsets video](https://github.com/trohit/leetcode/blob/main/images/subsets.PNG)](https://neetcode.io/courses/advanced-algorithms/11)

## combination
## permutation
