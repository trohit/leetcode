# Backtracking
## https://brilliant.org/wiki/recursive-backtracking/

| backtracking type  | Total Number    | Mnemonic           | Eg.                                | Time Complexity       | Space Complexity |
| -------------------| --------------- |--------------------|------------------------------------|-----------------------|------------------- 
| Permutations       | n!              | factorial          | [1,2],[2,1] are diff perms         | O(n!)                 | O(n.n!)          |
| Combinations       | n!/(n-k)!*k!    | n elms,k slots nCk | [1,2] and [2,1] are the same combo | O(k.2^n), O(k*C(n,k)) |                  |
| Subsets            | O(2^n)          | to choose or !     | [], [1]                            | O(n * 2^n)            |                  |

Mnemonic poems to remember max items (*SCP*)
- *Perms are factorials*
- *Combos are n-Choose-k*
- *Subsets are twice as powerful exponentially*

![formula](https://github.com/trohit/leetcode/blob/main/images/backtracking.PNG)

## Permutations
1. Order matters and optionally repetitions allowed 
2. A combination lock is actually a permutation lock.
```python
# T:O(n!)
# S:O(n.n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perms(a, i, res):
            n = len(a)
            if i == n: # base case
                res.append(a.copy())
                return
            for j in range(i, n): # lazy mgr case
                a[i], a[j] = a[j], a[i]
                perms(a, i+1, res)
                a[i], a[j] = a[j], a[i]
                
        res = []
        perms(nums, 0, res)
        return res

```

```python
# T: O(n!)
# S: O(n.n!)
def perms(ll, st, end, res):
  # leaf node
  if st == end:
    res.append(ll.copy())
    return
    
  # lazy mgr node
  for i in range(0, end+1):
    ll[st], ll[i] = ll[i], ll[st]
    perms(ll, st, end, res)
    ll[st], ll[i] = ll[i], ll[st]

# main call
ll = [1,2,3]
permutations(ll, 0, len(ll)-1, res) 
```

------------
## Combinations
### https://www.enjoyalgorithms.com/blog/find-all-combinations-of-k-numbers

[1,2] is the the same as [2,1] as **in combinations, order doesnt matter and no repetitions allowed .**
T:O(C(n,k))

```python
# Brute Force method
# T: O(k.2^n)
# S: O(n.k) when k<n, time complecity lesser than this since not all n chars are used in a k combo.
def combination(ll, k):
    def combo(ll, i, sl, res, n, k):
        if len(sl) >= k:        # base case
            res.append(sl.copy())
            return
            
        if i > n: return

        for j in range(i, n):        # lazy mgr case
            sl.append(ll[j])
            combo(ll, j+1, sl, res, n, k, lvl+1)
            sl.pop()
    # fn
    res = []
    combo(ll, 0, [], res, len(ll), k)
    print(len(res))

# main
import sys
k = int(sys.argv[1])
ll = list(range(100,106))
combination(ll, k)
```

https://neetcode.io/courses/advanced-algorithms/12
Further Reading
https://medium.com/enjoy-algorithm/find-all-possible-combinations-of-k-numbers-from-1-to-n-88f8e3fad33c

------------
## Subsets
subsets: max items 2^n where n is the num of uniq items in the set.\
Time Complexity : O(n.2^n), as we can choose to take |take each of n elms and at the leaf node we will have 2^n items of (len n) each\
Space Complexity: O(n), as the total mem will be the height of the tree 1->2->3

at every elm, have a choice: to include or not to include

Watch Neetcode video: https://neetcode.io/courses/advanced-algorithms/11
[![Watch the subsets video](https://github.com/trohit/leetcode/blob/main/images/subsets.PNG)](https://neetcode.io/courses/advanced-algorithms/11)

