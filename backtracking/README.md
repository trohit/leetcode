# Backtracking
## https://brilliant.org/wiki/recursive-backtracking/
## https://en.wikipedia.org/wiki/Backtracking

1. Goal, Choices and Constraints
2. root, accept, reject, first, next, output
3. base_case|leaf_node, lazy_mgr|nested_node

```python
def backtrack(res, args):
    if reached_goal():
        add_soln_to_res()
        return
        
    for i in range(choices):
        make_choices(i)
        backtrack(res, args)
        undo_choices(i)
```

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
#!/usr/bin/env python3
def perms(a, l, r, res):
    # leaf node
    if l == r:                      # accept
        slate = tostr(a)            
        #res.append(a.copy())
        res.append("".join(a))      # output
        return
    # lazy mgr node
    for i in range(l, r):           # choices, first, next
        a[i], a[l] = a[l], a[i]
        perms(a, l+1, r, res)       
        a[i], a[l] = a[l], a[i]     # backtrack
#main
s = input("enter str:")
res, a = [], list(s)
perms(a, 0, len(a), res)
print(res)
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

![combo](https://github.com/trohit/leetcode/blob/main/images/combos.png) "Combos")

```python
# Optimal improved combo method
# T: O(k.2^n)
# S: O(n.k) when k<n, time complexity lesser than this since not all n chars are used in a k combo.
"""
Only makes valid choices by using the j loop to kickoff from 1..n
That way no invalid choices need to be made.
"""
def combination(ll, k):
    def combo(ll, i, sl, res, n, k):
        if len(sl) >= k:        # base case
            res.append(sl.copy())
            return
            
        if i > n: return

        for j in range(i, n):        # lazy mgr case
            sl.append(ll[j])
            combo(ll, j+1, sl, res, n, k)
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

```python
"""
Simple combination implementation, using classical backtracking and no optimization
"""
def combo(ll:list, i:int, sl:list, res:list, k:int)->None:
    # base case
    if len(sl) == k:
        # tsl = "".join(sl) # only for easier representation
        # res.append(tsl)
        res.append(sl.copy())
        return

    if i == len(ll):
        return

    # lazy mgr / nested node case
    ## choose i
    sl.append(ll[i])
    combo(ll, i+1, sl, res, k)
    sl.pop() # undo selection

    ## do not choose i
    combo(ll, i+1, sl, res, k)

def combinations(ll, k):
    res = []
    combo(ll, 0, [], res, k)
    return res

# driver 
# ./combo abcde 3
import sys
argc = len(sys.argv)
ll = [c for c in sys.argv[1]]
k = int(sys.argv[2])
res = combinations(ll, k) # where len(ll) is n
print(res)
print(len(res))
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

```python
# T:O(2^n)
# S:O(n.2^n)
def subsets(a):
    def subs(a, i, sl, res):
        # base case
        # as elm can be skipped len(st) can be < len(a)
        if len(sl) == len(a) or i >= len(a):
            res.append(sl.copy())
            return

        # lazy mgr case
        sl.append(a[i])
        subs(a, i+1, sl, res)
        sl.pop()
        subs(a, i+1, sl, res)

    res, sl = [], []
    subs(a, 0, sl, res)
    return res
    
# driver code
import sys
st = sys.argv[1] # "abc"
a = [x for x in st]
res = subsets(a)
print(len(res))
```

## Problems
https://leetcode.com/problems/permutations/

https://leetcode.com/problems/permutations-ii/


https://leetcode.com/problems/combinations/

https://leetcode.com/problems/combination-sum-ii/

https://leetcode.com/problems/combination-sum-iii/


https://leetcode.com/problems/subsets/

https://leetcode.com/problems/subsets-ii/

https://leetcode.com/problems/palindrome-partitioning/
