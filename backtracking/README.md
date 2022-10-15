# Backtracking

| backtracking type  | Total Number    | Mnemonic           | Eg.                                | Time Complexity       | Space Complexity |
| -------------------| --------------- |--------------------|------------------------------------|-----------------------|------------------- 
| Subsets            | O(2^n)          | to choose or !     | [], [1]                            | O(n * 2^n)            |                  |
| Combinations       | n!/(n-k)!*k!    | n elms,k slots nCk | [1,2] and [2,1] are the same combo | O(k.2^n), O(k*C(n,k)) |                  |
| Permutations       | n!              | factorial          | [1,2],[2,1] are diff perms         | O(n!)                 | O(n.n!)          |

Mnemonic poems to remember max items (*SCP*)
- *Subsets are twice as powerful exponentially*
- *Combos are n-Choose-k*
- *Perms are factorials*

![formula](https://github.com/trohit/leetcode/blob/main/images/backtracking.PNG)

## Subsets
subsets: max items 2^n where n is the num of uniq items in the set.\
Time Complexity : O(n.2^n), as we can choose to take |take each of n elms and at the leaf node we will have 2^n items of (len n) each\
Space Complexity: O(n), as the total mem will be the height of the tree 1->2->3

at every elm, have a choice: to include or not to include

Watch Neetcode video: https://neetcode.io/courses/advanced-algorithms/11
[![Watch the subsets video](https://github.com/trohit/leetcode/blob/main/images/subsets.PNG)](https://neetcode.io/courses/advanced-algorithms/11)

## Combinations
[1,2] is the the same as [2,1] as **in combinations, order doesnt matter and no repetitions allowed .**
T:O(C(n,k))

https://neetcode.io/courses/advanced-algorithms/12
Further Reading
https://medium.com/enjoy-algorithm/find-all-possible-combinations-of-k-numbers-from-1-to-n-88f8e3fad33c

## Permutations
** Order matters and optionally repetitions allowed **
A combination lock is actually a permutation lock.
